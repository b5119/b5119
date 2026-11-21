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
    """Doom-themed animated chart: bars charge up in sequence, then reset and loop."""
    top = weights.most_common(TOP_N)
    total = sum(w for _, w in top) or 1
    biggest = top[0][1] if top else 1
    width, row_h, track_x, track_w = 380, 21, 118, 190
    height = 62 + row_h * len(top) + 14
    font = "'Fira Code','JetBrains Mono',Consolas,monospace"
    out = [
        f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
        'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Most used languages, weighted by commits">',
        '<defs>'
        '<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0e1a14"/><stop offset="1" stop-color="#060908"/></linearGradient>'
        '<linearGradient id="bar" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#1f7a46"/><stop offset="1" stop-color="#3ddc84"/></linearGradient>'
        '<filter id="glow" x="-30%" y="-80%" width="160%" height="260%"><feGaussianBlur stdDeviation="2" result="b"/>'
        '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
        '</defs>',
        f'<rect x="0.75" y="0.75" width="{width - 1.5}" height="{height - 1.5}" rx="8" fill="url(#bg)" stroke="#1f3a2b" stroke-width="1.5"/>',
        f'<text x="20" y="30" font-family="{font}" font-size="14" font-weight="700" letter-spacing="3" fill="#3ddc84">ARSENAL</text>',
        f'<text x="20" y="46" font-family="{font}" font-size="9.5" letter-spacing="1" fill="#c9a227">most used languages · weighted by commits</text>',
        f'<path d="M20 52 H{width - 20}" stroke="#1f3a2b" stroke-width="1"/>',
        f'<path d="M20 52 H90" stroke="#c9a227" stroke-width="1.5"/>',
    ]
    for i, (lang, w) in enumerate(top):
        y = 62 + i * row_h
        pct = 100 * w / total
        fill_w = track_w * w / biggest
        delay = f"{i * 0.18:.2f}s"
        out.append(f'<circle cx="26" cy="{y + 9}" r="4" fill="{colors[lang]}"/>')
        out.append(f'<text x="38" y="{y + 12.5}" font-family="{font}" font-size="11" fill="#cfe8d8">{escape(lang)}</text>')
        out.append(f'<rect x="{track_x}" y="{y + 5}" width="{track_w}" height="8" rx="4" fill="#13261b"/>')
        out.append(
            f'<rect x="{track_x}" y="{y + 5}" width="0" height="8" rx="4" fill="url(#bar)" filter="url(#glow)">'
            f'<animate attributeName="width" values="0;{fill_w:.1f};{fill_w:.1f};0" keyTimes="0;0.14;0.9;1" '
            f'dur="9s" begin="{delay}" repeatCount="indefinite" calcMode="spline" keySplines="0.2 0.8 0.2 1;0 0 1 1;0.4 0 1 1"/></rect>'
        )
        out.append(
            f'<text x="{width - 20}" y="{y + 12.5}" text-anchor="end" font-family="{font}" font-size="10.5" fill="#3ddc84" opacity="0">{pct:.1f}%'
            f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.14;0.9;1" dur="9s" begin="{delay}" repeatCount="indefinite"/></text>'
        )
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
