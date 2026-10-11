#!/usr/bin/env python3
"""Generate assets/top-langs.svg: most used languages weighted by commits.

For every repo the token can access (own, collaborator, org; private included),
the user's commits on the default branch are counted and each commit is split
across that repo's languages in proportion to their bytes. Needs GH_TOKEN (a PAT with `repo` scope to see
private repos) and optionally GH_USER / OUT.
"""
import json
import os
import time
import urllib.request
from collections import Counter
from html import escape

USER = os.environ.get("GH_USER", "b5119")
OUT = os.environ.get("OUT", "assets/top-langs.svg")
TOKEN = os.environ["GH_TOKEN"]
EXCLUDE = {"Jupyter Notebook"}
TOP_N = 10

QUERY = """
query($login: String!, $after: String) {
  user(login: $login) {
    id
    repositories(first: 50, after: $after, ownerAffiliations: [OWNER, COLLABORATOR, ORGANIZATION_MEMBER]) {
      pageInfo { hasNextPage endCursor }
      nodes {
        nameWithOwner
        isFork
        parent { nameWithOwner }
        languages(first: 15, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name color } }
        }
        defaultBranchRef { name }
      }
    }
  }
}
"""

HISTORY = """
query($owner: String!, $name: String!, $id: ID!) {
  repository(owner: $owner, name: $name) {
    defaultBranchRef { target { ... on Commit { history(author: {id: $id}) { totalCount } } } }
  }
}
"""

# Colours mirror the github_dark card; unknown languages fall back to grey.
FALLBACK = "#8b949e"


def gql(query, variables):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variables}).encode(),
        headers={"Authorization": f"bearer {TOKEN}", "User-Agent": "top-langs"},
    )
    for attempt in range(3):
        with urllib.request.urlopen(req, timeout=60) as r:
            body = json.load(r)
        if "errors" not in body:
            return body["data"]
        time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"GraphQL error: {body['errors']}")


def collect():
    """Weight languages by the user's own commits on each accessible repo."""
    weights, colors, repos = Counter(), {}, {}
    after, uid, nodes = None, None, []
    while True:
        user = gql(QUERY, {"login": USER, "after": after})["user"]
        uid = user["id"]
        nodes += user["repositories"]["nodes"]
        page = user["repositories"]["pageInfo"]
        if not page["hasNextPage"]:
            break
        after = page["endCursor"]
    names = {r["nameWithOwner"] for r in nodes}
    for repo in nodes:
        # A fork of a repo that is also listed would count the same work twice.
        if repo["isFork"] and repo["parent"] and repo["parent"]["nameWithOwner"] in names:
            continue
        ref = repo["defaultBranchRef"]
        if not ref or not repo["languages"]["edges"]:
            continue
        owner, name = repo["nameWithOwner"].split("/")
        try:
            h = gql(HISTORY, {"owner": owner, "name": name, "id": uid})
        except RuntimeError:
            print(f"skipped {repo['nameWithOwner']} (history query failed)")
            continue
        commits = h["repository"]["defaultBranchRef"]["target"]["history"]["totalCount"]
        if not commits:
            continue
        repos[repo["nameWithOwner"]] = commits
        edges = repo["languages"]["edges"]
        total = sum(e["size"] for e in edges) or 1
        for e in edges:
            lang = e["node"]["name"]
            if lang in EXCLUDE:
                continue
            colors.setdefault(lang, e["node"]["color"] or FALLBACK)
            weights[lang] += commits * e["size"] / total
    return weights, colors, repos


def render(weights, colors):
    top = weights.most_common(TOP_N)
    total = sum(w for _, w in top) or 1
    width, bar_x, bar_w = 300, 25, 250
    height = 55 + 25 * ((len(top) + 1) // 2) + 25
    out = [
        f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
        'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Most used languages, weighted by commits">',
        f'<rect width="{width}" height="{height}" rx="4.5" fill="#0d1117"/>',
        '<text x="25" y="35" font-family="Segoe UI, Ubuntu, sans-serif" font-size="18" font-weight="600" fill="#58a6ff">Most Used Languages</text>',
    ]
    x = bar_x
    for i, (lang, w) in enumerate(top):
        seg = bar_w * w / total
        col = colors[lang]
        if i == 0 or i == len(top) - 1:
            # rounded end cap: a rounded rect plus a square one over its inner half
            out.append(f'<rect x="{x:.2f}" y="55" width="{seg:.2f}" height="8" rx="4" fill="{col}"/>')
            sq_x = x + seg / 2 if i == 0 else x
            out.append(f'<rect x="{sq_x:.2f}" y="55" width="{seg / 2:.2f}" height="8" fill="{col}"/>')
        else:
            out.append(f'<rect x="{x:.2f}" y="55" width="{seg:.2f}" height="8" fill="{col}"/>')
        x += seg
    for i, (lang, w) in enumerate(top):
        cx = 25 + (i % 2) * 125
        cy = 85 + (i // 2) * 25
        out.append(f'<circle cx="{cx + 5}" cy="{cy - 4}" r="5" fill="{colors[lang]}"/>')
        out.append(f'<text x="{cx + 15}" y="{cy}" font-family="Segoe UI, Ubuntu, sans-serif" font-size="11" fill="#c9d1d9">{escape(lang)} {100 * w / total:.2f}%</text>')
    out.append("</svg>")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    weights, colors, repos = collect()
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    with open(OUT, "w") as f:
        f.write(render(weights, colors))
    print(f"{len(repos)} repos, {sum(repos.values())} commits")
    for r, n in sorted(repos.items(), key=lambda kv: -kv[1])[:15]:
        print(f"  {n:5d}  {r}")
    for lang, w in weights.most_common(TOP_N):
        print(f"  {lang:12s} {w:8.1f}")
