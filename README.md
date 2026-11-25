<!-- Header -->
<p align="center">
  <img src="./assets/doom-banner.svg?v=6" alt="Frank Bwalya — Systems Thinker, Backend & Distributed Systems" width="900"/>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/frank-bwalya-64b124275">
    <img src="./assets/badges/linkedin.svg" alt="LinkedIn"/>
  </a>
  <a href="mailto:bwalyafrank61@gmail.com">
    <img src="./assets/badges/email.svg" alt="Email"/>
  </a>
  <img src="https://komarev.com/ghpvc/?username=b5119&style=for-the-badge&color=2EA043&label=PROFILE+VIEWS"/>
</p>

<p align="center"><img src="./assets/doom-divider.svg?v=2" width="860" alt=""/></p>

## ◈ The Mindset

> Most developers build features. I'm learning to design **systems**.

Anyone can assemble parts and get something that runs. The harder question, and the one I care about, is what makes the assembly *hold*: what keeps it coherent when connections drop, when data conflicts, and when the people depending on it can't see inside. I'm a software engineering student working toward that, with a focus on **backend architecture**, **distributed application design** and **blockchain infrastructure**.

A system, like a person, is more than its components. It is the memory it keeps, the decisions it can explain and the promises it holds under pressure. My trajectory is to grow from a developer who builds applications into an engineer who designs the **structures** those applications run on.

```
surface-level dev  →  application builder  →  [current]  →  system architect
```

<p align="center"><img src="./assets/doom-divider.svg?v=2" width="860" alt=""/></p>

## ◈ At a Glance

<p align="center">
  <img src="./assets/glance.svg?v=1" alt="1st place at the 2026 ZAMREN Student Hackathon · 100+ merged pull requests across 11 repositories · 100+ tests in Nexus · 17 architecture decision records" width="900"/>
</p>

🎓 **Studying** BSc Software Engineering, ZCAS University (final year) &nbsp;·&nbsp; 🔎 **Open to** software engineering internships across systems, backend, blockchain and mobile, and open-source collaboration

<p align="center"><img src="./assets/doom-divider.svg?v=2" width="860" alt=""/></p>

## ◈ What I'm Actually Working On

*These are two of the several things I'm working on at any one time. Alongside them sit team and client builds in private repositories, coursework and open-source contributions. These two are the ones I can show and walk through.*

<p align="center">
  <img src="./assets/card-nexus.svg?v=2" alt="Nexus — personal device mesh built in Rust" width="900"/>
</p>

#### `01` — Nexus — Personal Device Mesh *(Active · file mesh and screen streaming working; Android file access designed)*
> *Paired devices, one authenticated mesh — filesystem, streaming, migration*

A **personal device mesh** built from scratch in **Rust**: mount any paired
device's storage as a real FUSE filesystem, stream its screen over an
authenticated gRPC channel, and migrate app state between devices — all over
an mTLS-encrypted, code-paired connection.

- **Lazy FUSE virtualization** — remote files appear local; bytes move on
  demand, not on mount. Multi-writer conflict detection via vector clocks —
  concurrent edits keep both versions, never silently lose data.
- **Device pairing** — 6-digit code exchange, per-device identity certificates,
  mTLS on every connection. Proven on a real Android phone → Linux laptop mount,
  byte-exact including chunk-boundary offset reads.
- **Screen streaming** — H.264 encode (QSV/libx264 fallback) → gRPC
  bidirectional stream → decode + winit display, with raw uinput input injection.
- **Migration SDK** — app-cooperative state migration with three conflict
  policies (LastWriteWins / AppMerge / KeepBoth), Android JNI bindings via
  the `jni` crate.
- **Engineering discipline** — 100+ tests, CI-gated on every PR (build + test +
  fmt + clippy), branch-protected main, 17 ADRs documenting every real
  constraint hit along the way.

Stack: `Rust` · `Tokio` · `gRPC/tonic` · `FUSE` · `ffmpeg` · `PipeWire` ·
`TLS/mTLS` · `Android (cargo-ndk)`
[→ View Repository](https://github.com/b5119/nexus)  
Related: an ext4 partition-recovery case study (read-only diagnosis, device-mapper stitching, zero data lost).

<p align="center"><img src="./assets/doom-divider.svg?v=2" width="860" alt=""/></p>

<p align="center">
  <img src="./assets/card-cdf.svg?v=2" alt="CDF SigTrace — blockchain-anchored public-spending checks, final-year project" width="900"/>
</p>

### `02` — CDF SigTrace — Blockchain Accountability Framework *(Final-year project · prototype complete)*
> *Making public money provable, not just trackable*

A **blockchain-anchored accountability framework** for Zambia's Constituency Development Fund and government procurement — two systems, **SigTrace** (procurement contract integrity) and **CDF Pulse** (field-delivery verification), joined by a monitor that flags ghost projects.

- **Dual-ledger anchoring** — Hyperledger Fabric for institutional membership, Polygon for citizen-verifiable confirmations *(both simulated in the prototype; no live institutional data yet)*
- **Privacy by architecture** — personal data stays off-chain; only hashes and non-personal metadata are written
- **Risk signals, not verdicts** — every analytical output is a flag requiring human review, never a determination of wrongdoing
- **Offline-first field app** — CDF Pulse PWA for delivery verification where connectivity isn't guaranteed

Stack: `Python` · `FastAPI` · `PostgreSQL` · `Solidity` · `Hyperledger Fabric` · `Polygon` · `React`  
Focus: Civic-tech transparency under real infrastructure constraints.  
🌐 [Live demo (demonstration data)](https://cdf-backend-0ued.onrender.com/) · 🔒 Source private — walkthrough available on request

<p align="center"><img src="./assets/doom-divider.svg?v=2" width="860" alt=""/></p>

## ◈ Technical Stack

<div align="center">

<table>
<tr>
<td align="left" nowrap><b>Languages</b><br/><sub>what I ship in</sub></td>
<td align="left"><img src="https://skillicons.dev/icons?i=rust,go,python,ts,js,dart,kotlin,solidity&theme=dark" alt="Rust, Go, Python, TypeScript, JavaScript, Dart, Kotlin, Solidity"/><br/><img src="https://skillicons.dev/icons?i=java,cs,php,bash,sql&theme=dark" alt="Java, C#, PHP, Bash, SQL"/></td>
</tr>
<tr>
<td align="left" nowrap><b>Backend & APIs</b><br/><sub>services and contracts</sub></td>
<td align="left"><img src="https://skillicons.dev/icons?i=fastapi,flask,laravel,nodejs,dotnet,swagger&theme=dark" alt="FastAPI, Flask, Laravel, Node.js, .NET, Swagger"/><br/><img src="./assets/badges/go-chi.svg" alt="go-chi"/> <img src="./assets/badges/openapi.svg" alt="openapi"/> <img src="./assets/badges/grpc.svg" alt="grpc"/> <img src="./assets/badges/protobuf.svg" alt="protobuf"/></td>
</tr>
<tr>
<td align="left" nowrap><b>Systems</b><br/><sub>low-level and distributed</sub></td>
<td align="left"><img src="./assets/badges/tokio.svg" alt="tokio"/> <img src="./assets/badges/fuse.svg" alt="fuse"/> <img src="./assets/badges/grpc.svg" alt="grpc"/> <img src="./assets/badges/protobuf.svg" alt="protobuf"/> <img src="./assets/badges/tailscale.svg" alt="tailscale"/> <img src="./assets/badges/ssh.svg" alt="ssh"/></td>
</tr>
<tr>
<td align="left" nowrap><b>Blockchain</b><br/><sub>contracts and anchoring</sub></td>
<td align="left"><img src="https://skillicons.dev/icons?i=solidity,hardhat&theme=dark" alt="Solidity, Hardhat"/><br/><img src="./assets/badges/hyperledger-fabric.svg" alt="hyperledger-fabric"/> <img src="./assets/badges/polygon.svg" alt="polygon"/> <img src="./assets/badges/ipfs.svg" alt="ipfs"/></td>
</tr>
<tr>
<td align="left" nowrap><b>Frontend & Mobile</b><br/><sub>web and cross-platform</sub></td>
<td align="left"><img src="https://skillicons.dev/icons?i=flutter,dart,react,angular,kotlin,tailwind,bootstrap,vite&theme=dark" alt="Flutter, Dart, React, Angular, Kotlin, Tailwind, Bootstrap, Vite"/></td>
</tr>
<tr>
<td align="left" nowrap><b>Data</b><br/><sub>storage</sub></td>
<td align="left"><img src="https://skillicons.dev/icons?i=postgres,sqlite,mongodb,firebase,supabase&theme=dark" alt="PostgreSQL, SQLite, MongoDB, Firebase, Supabase"/></td>
</tr>
<tr>
<td align="left" nowrap><b>Infra & Tooling</b><br/><sub>delivery and workflow</sub></td>
<td align="left"><img src="https://skillicons.dev/icons?i=docker,aws,githubactions,linux,ubuntu,git,neovim,vscode&theme=dark" alt="Docker, AWS, GitHub Actions, Linux, Ubuntu, Git, Neovim, VS Code"/></td>
</tr>
<tr>
<td align="left" nowrap><b>Integrating in 2026</b><br/><sub>actively learning</sub></td>
<td align="left"><img src="https://skillicons.dev/icons?i=kubernetes,kafka,graphql,redis&theme=dark" alt="Kubernetes, Kafka, GraphQL, Redis"/></td>
</tr>
</table>

</div>

<p align="center"><img src="./assets/doom-divider.svg?v=2" width="860" alt=""/></p>

## ◈ The Architecture

```python
class FrankBwalya:
    """
    Software Engineering Student → System Architect in Training
    Lusaka, Zambia | 2026
    """

    trajectory = [
        "application-level development",     # ✅ done
        "backend architecture & patterns",   # ✅ done
        "smart contract ecosystems",         # ✅ done — ChainBa (3 contracts, 23 tests)
        "distributed systems design",        # ← currently here
        "full system architecture",          # 🎯 destination
    ]

    engineering_focus = {
        "systems":     ["Rust", "Tokio", "gRPC", "FUSE", "cross-compilation"],
        "backend":     ["FastAPI", "Flask", "Laravel", "Go (chi)", "OpenAPI / Swagger", "service-layer design"],
        "blockchain":  ["Solidity", "Hardhat", "OpenZeppelin", "ethers.js", "dApp delivery"],
        "civic_tech":  ["digital identity (ZedLedger)", "gov accountability (SigTrace)", "data-protection compliance"],
        "mobile":      ["Flutter", "Dart", "Android (cargo-ndk)", "offline-first PWAs"],
        "devops":      ["Docker", "AWS deployment", "Tailscale + SSH", "CI/CD", "environment-based configuration"],
    }

    principle = (
        "I am intentionally refining previous systems rather than chasing new ones. "
        "Architectural depth over surface-level expansion."
    )

    def current_question(self) -> str:
        return "Not 'how do I build this?' — but 'how should this be designed?'"
```

<p align="center"><img src="./assets/doom-divider.svg?v=2" width="860" alt=""/></p>

## ◈ GitHub Statistics

<p align="center">
  <img src="https://github-readme-stats-b5119.vercel.app/api?username=b5119&show_icons=true&theme=github_dark&hide_border=true&border_color=1f3a2b&bg_color=0b1410&title_color=3ddc84&icon_color=c9a227&text_color=cfe8d8&include_all_commits=true&count_private=true&rank_icon=letters" width="495"/>
</p>

<p align="center">
  <img src="./assets/top-langs.svg?v=2" alt="Most used languages, weighted by commits across all repos I contribute to" width="380"/>
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=b5119&theme=github-dark-blue&hide_border=true&background=0b1410&ring=3ddc84&fire=c9a227&currStreakNum=cfe8d8&sideNums=cfe8d8&currStreakLabel=3ddc84&sideLabels=3ddc84&dates=8fb9a0" width="750"/>
</p>

<p align="center">
  <img src="https://activity-graph.vercel.app/graph?username=b5119&bg_color=0b1410&color=8fb9a0&line=3ddc84&point=c9a227&area=true&hide_border=true" width="750"/>
</p>

<p align="center"><img src="./assets/doom-divider.svg?v=2" width="860" alt=""/></p>

## ◈ More of My Work

### 🏆 ZedLedger — Zambia eNID Platform *(Hackathon Winner)*
> *1st place · Zambia Digital ID category · 2026 ZAMREN Student Hackathon, Livingstone*

<p align="center">
  <img src="./assets/zedledger.svg" alt="ZedLedger — Zambia eNID Platform. 1st prize, Zambia Digital ID category, 2026 ZAMREN Student Hackathon." width="860"/>
</p>

A full-stack **digital national identity platform** for Zambia, built by a team of four under hackathon conditions — citizen registration, eNID issuance, civil registration (births/deaths), and blockchain-anchored certificates.

- **Backend lead** — I owned the identity, mobile-money (GSB / ISO 8583), immigration, blockchain, and API-gateway services
- **Microservice architecture** — seven services behind a single JWT-validating API gateway, with isolated PostgreSQL schemas per domain
- **On-chain integrity** — Hyperledger Fabric anchors tamper-evident certificate hashes for births, deaths, and IDs
- **Compliance by design** — aligned with the Zambia Data Protection Act No. 3 of 2021

Stack: `Next.js` · `Python` · `FastAPI` · `Hyperledger Fabric` · `PostgreSQL` · `Docker`  
🔒 Private (hackathon repo) — walkthrough available on request

<p align="center"><img src="./assets/doom-divider.svg?v=2" width="860" alt=""/></p>

<p align="center"><img src="./assets/doom-divider.svg?v=2" width="860" alt=""/></p>

> Plus breadth across backend, blockchain, and mobile:

<p align="center">
  <a href="https://github.com/b5119/flask-api-dashboard">
    <img src="https://github-readme-stats-b5119.vercel.app/api/pin/?username=b5119&repo=flask-api-dashboard&theme=github_dark&hide_border=true&border_color=1f3a2b&bg_color=0b1410&title_color=3ddc84&icon_color=c9a227&text_color=cfe8d8" />
  </a>
  <a href="https://github.com/b5119/chainba">
    <img src="https://github-readme-stats-b5119.vercel.app/api/pin/?username=b5119&repo=chainba&theme=github_dark&hide_border=true&border_color=1f3a2b&bg_color=0b1410&title_color=3ddc84&icon_color=c9a227&text_color=cfe8d8" />
  </a>
</p>

<p align="center">
  <a href="https://github.com/b5119/gpa_tracker">
    <img src="https://github-readme-stats-b5119.vercel.app/api/pin/?username=b5119&repo=gpa_tracker&theme=github_dark&hide_border=true&border_color=1f3a2b&bg_color=0b1410&title_color=3ddc84&icon_color=c9a227&text_color=cfe8d8" />
  </a>
  <a href="https://github.com/b5119/python-api-projects">
    <img src="https://github-readme-stats-b5119.vercel.app/api/pin/?username=b5119&repo=python-api-projects&theme=github_dark&hide_border=true&border_color=1f3a2b&bg_color=0b1410&title_color=3ddc84&icon_color=c9a227&text_color=cfe8d8" />
  </a>
</p>

<p align="center"><img src="./assets/doom-divider.svg?v=2" width="860" alt=""/></p>

## ◈ 2026 Engineering Growth & Collaboration

### Technical Growth Areas

I am actively deepening expertise in:

- **Distributed systems principles** — consistency models, fault tolerance, replication strategies
- **Scalable backend design** — service boundaries, load patterns, API contract discipline
- **Smart contract security** — audit patterns, invariant testing, formal verification concepts
- **Containerization & deployment** — Docker, CI/CD pipeline design, environment management
- **Test-driven backend development** — integration testing, contract testing, coverage discipline
- **Data modeling for decision systems** — schema design that reflects domain logic, not just storage

The objective is not tool accumulation. It is **architectural fluency**.

### Collaboration & Internship Intent

I am actively seeking:

- **Backend engineering internships** — production exposure across real system constraints
- **Distributed systems research collaboration** — theory applied to implementation
- **Blockchain infrastructure projects** — smart contract ecosystems with genuine use cases
- **Open-source backend contributions** — meaningful PRs, not surface-level fixes

If you are building structured, scalable systems — I am interested in contributing seriously, not superficially.

📧 **bwalyafrank61@gmail.com** · 💼 [LinkedIn](https://www.linkedin.com/in/frank-bwalya-64b124275)

### Research Direction

My long-term interest areas converge around systems that operate under real-world constraints:

- **Trust modeling in decentralized environments** — what replaces institutional guarantees at the protocol level
- **System reliability under constrained infrastructure** — designing for contexts where resources and margin are limited
- **Backend architecture for emerging markets** — systems built for conditions, not assumptions
- **Data-informed decision systems** — where analytical modeling drives outcomes, not just dashboards

I am particularly interested in bridging **formal system design principles** with **production-level implementation** — closing the gap between theory and what actually ships.

### Forward Vision — The Roadmap

<!-- Animated roadmap: a data packet travels the track through each milestone on a loop.
     Source: assets/roadmap.svg (hand-authored animated SVG) -->
<p align="center">
  <img src="./assets/roadmap.svg?v=2" alt="Engineering roadmap — a data packet travels from Application Builder through Backend Engineer and Smart Contracts to Distributed Systems Engineer (current) toward Systems Architect" width="860"/>
</p>

<details>
<summary><b>How these percentages are measured</b></summary>

<br/>

Each phase is a checklist of evidence I can point to in a repository. Progress is items met divided by items in the list, so a bar only moves when a real milestone lands.

| Phase | Score | ✅ Met | ⬜ Not yet |
|:--|:--:|:--|:--|
| **01 · Application Builder** | **4 / 4** | App shipped to production (Skutopia) · REST API and dashboard · auth and persistence · automated tests | — |
| **02 · Backend Engineer** | **7 / 7** | Services with PostgreSQL migrations · contract-first OpenAPI · transactional payout and reconciliation logic · role-based access · CI on every PR · reviewing teammates' PRs · backend function live in production (Supabase Edge Function, Skutopia) | — |
| **03 · Smart Contracts & dApps** | **7 / 7** | Three contracts · 23-test suite · React dApp · Node/Express backend · OpenZeppelin patterns · deployment script · written security review | Next level, outside ChainBa's scope: public-testnet deployment and an independent audit |
| **04 · Distributed Systems Engineer** | **6 / 8** | gRPC service boundaries · mTLS device identity · vector-clock conflict detection · FUSE virtual filesystem · real-hardware cross-device test · 17 ADRs | Cross-device replication and sync · fault-injection or consensus work |
| **05 · Systems Architect** | **3 / 8** | Written design decisions (ADRs) · multi-service design from requirements · privacy and compliance by design | Load-tested system · operated in production · led architecture for a team in production · formally reasoned consistency model · incident ownership |

</details>


<p align="center">
  <b>Domains already shipped:</b><br/>
  <img src="./assets/badges/shipped-smart-contracts.svg" alt="Smart Contracts"/>
  <img src="./assets/badges/shipped-full-stack-dapp.svg" alt="Full-stack dApp"/>
  <img src="./assets/badges/shipped-backend-services.svg" alt="Backend services"/>
</p>

Not just code that runs. **Systems that endure.**

<p align="center"><img src="./assets/doom-divider.svg?v=2" width="860" alt=""/></p>

## ◈ Let's Connect

📧 **Email:** bwalyafrank61@gmail.com  
💼 **LinkedIn:** [Frank Bwalya](https://www.linkedin.com/in/frank-bwalya-64b124275)

<p align="center"><img src="./assets/doom-divider.svg?v=2" width="860" alt=""/></p>

## ◈ The Quote I Keep Coming Back To

> *"Knowledge is a paradox. The more we understand, the more we realize the vastness of our ignorance."*
>
> **— Viktor, Arcane**

That isn't discouragement. It's the only honest description of what engineering actually is — a permanent state of knowing enough to understand how much remains. The engineers worth learning from aren't the ones who know the most. They're the ones who've stayed long enough to understand *how much they don't know* — and kept building anyway.

<p align="center">
  <img src="https://img.shields.io/github/followers/b5119?label=Followers&style=social"/>
  &nbsp;
  <img src="https://img.shields.io/github/stars/b5119?label=Stars&style=social"/>
</p>

<p align="center">
  <sub>Last updated: November 2026 · Lusaka, Zambia · Built with deliberate intent, not just enthusiasm ☕</sub>
</p>
