<!-- Header -->
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&duration=3000&pause=900&color=58A6FF&background=FFFFFF00&center=true&vCenter=true&multiline=true&width=750&height=100&lines=Frank+Bwalya+%E2%80%94+Systems+Thinker;Distributed+Systems+Engineer+in+Training+%7C+Lusaka%2C+Zambia;Building+Structure+Before+Building+Features" alt="Typing SVG"/>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/frank-bwalya-64b124275">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>
  </a>
  <a href="mailto:bwalyafrank61@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/>
  </a>
  <img src="https://komarev.com/ghpvc/?username=b5119&style=for-the-badge&color=58A6FF&label=PROFILE+VIEWS"/>
</p>

---

## ◈ The Mindset

> Most developers build features. I'm learning to design **systems**.

I'm a software engineering student at the stage where the interesting questions shift — from *"how do I make this work?"* to *"how do I make this hold?"* My focus is on **backend architecture**, **distributed application design**, and **blockchain infrastructure**. I'm not chasing breadth. I'm deliberately deepening.

My current trajectory: grow from a developer who builds applications into an engineer who designs the **structures** those applications run on.

```
surface-level dev  →  application builder  →  [current]  →  system architect
```

---

## ◈ What I'm Actually Working On

### `01` — Nexus — Personal Device Mesh *(Active)*
> *Your devices, one filesystem — nothing copied until it's read*

A **personal device mesh** built from scratch in **Rust**: mount your phone's storage on your laptop as a real, lazy-loaded FUSE filesystem. `ls`, `cat`, `cp` all behave like a local directory — but nothing transfers until you actually read it.

- **Lazy FUSE virtualization** — remote files appear local; bytes move on demand, not on mount
- **Typed gRPC transport** — a `FileService` contract (ListDir / Stat / ReadFile) over Tonic + Prost
- **Cross-compiled to Android** — `cargo-ndk`, arm64-v8a; the host role runs on-device
- **Hardware-verified** — byte-exact reads across a real phone → laptop mount, including chunk-boundary offset reads

Stack: `Rust` · `Tokio` · `gRPC` · `Protobuf` · `FUSE`  
Focus: Systems programming where correctness is measured in bytes.  
[→ View Repository](https://github.com/b5119/nexus02)

---

### `02` — CDF SigTrace — Blockchain Accountability Framework *(In Progress)*
> *Making public money provable, not just trackable*

A **blockchain-anchored accountability framework** for Zambia's Constituency Development Fund and government procurement — two systems, **SigTrace** (procurement contract integrity) and **CDF Pulse** (field-delivery verification), joined by a monitor that flags ghost projects.

- **Dual-ledger anchoring** — Hyperledger Fabric for institutional membership, Polygon for citizen-verifiable confirmations
- **Privacy by architecture** — personal data stays off-chain; only hashes and non-personal metadata are written
- **Risk signals, not verdicts** — every analytical output is a flag requiring human review, never a determination of wrongdoing
- **Offline-first field app** — CDF Pulse PWA for delivery verification where connectivity isn't guaranteed

Stack: `Python` · `FastAPI` · `PostgreSQL` · `Solidity` · `Hyperledger Fabric` · `Polygon` · `React`  
Focus: Civic-tech transparency under real infrastructure constraints.  
[→ View Repository](https://github.com/b5119/cdf-sigtrace-zambia)

---

## ◈ Technical Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=rust,python,dart,ts,js,solidity,html,css&theme=dark&perline=8" /><br/>
  <img src="https://skillicons.dev/icons?i=fastapi,flask,flutter,react,tailwind,nodejs,hardhat,vite&theme=dark&perline=8" /><br/>
  <img src="https://skillicons.dev/icons?i=postgres,docker,kubernetes,git,github,githubactions,linux,vscode&theme=dark&perline=8" />
</p>

<br/>

### Core Languages

<div align="center">

![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Dart](https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white)
![Solidity](https://img.shields.io/badge/Solidity-363636?style=for-the-badge&logo=solidity&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white)

</div>

### Systems & Backend

<div align="center">

![Tokio](https://img.shields.io/badge/Tokio-000000?style=for-the-badge&logo=rust&logoColor=white)
![gRPC](https://img.shields.io/badge/gRPC-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Protobuf](https://img.shields.io/badge/Protobuf-EA4335?style=for-the-badge&logo=protobuf&logoColor=white)
![FUSE](https://img.shields.io/badge/FUSE-EE0000?style=for-the-badge&logo=linux&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)

</div>

### Blockchain & Frontend

<div align="center">

![Hardhat](https://img.shields.io/badge/Hardhat-FFF100?style=for-the-badge&logo=ethereum&logoColor=black)
![Hyperledger](https://img.shields.io/badge/Hyperledger_Fabric-2F3134?style=for-the-badge&logo=hyperledger&logoColor=white)
![Polygon](https://img.shields.io/badge/Polygon-7B3FE4?style=for-the-badge&logo=polygon&logoColor=white)
![IPFS](https://img.shields.io/badge/IPFS-65C2CB?style=for-the-badge&logo=ipfs&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Flutter](https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)

</div>

### Infrastructure & Tooling

<div align="center">

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux_(Ubuntu)-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

</div>

### Learning / Integrating in 2026

<div align="center">

![Cloud](https://img.shields.io/badge/Cloud_Deployment-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![GraphQL](https://img.shields.io/badge/GraphQL-E10098?style=for-the-badge&logo=graphql&logoColor=white)

</div>

---

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
        "distributed systems design",        # ← currently here
        "smart contract ecosystems",         # ⬜ in progress
        "full system architecture",          # 🎯 destination
    ]

    engineering_focus = {
        "systems":     ["Rust", "Tokio", "gRPC", "FUSE", "cross-compilation"],
        "backend":     ["FastAPI", "Flask", "service-layer design", "API orchestration"],
        "blockchain":  ["Solidity", "Hyperledger Fabric", "Polygon", "on-chain anchoring"],
        "mobile":      ["Flutter", "Dart", "Android (cargo-ndk)", "offline-first PWAs"],
        "devops":      ["Docker", "CI/CD", "environment-based configuration"],
    }

    principle = (
        "I am intentionally refining previous systems rather than chasing new ones. "
        "Architectural depth over surface-level expansion."
    )

    def current_question(self) -> str:
        return "Not 'how do I build this?' — but 'how should this be designed?'"
```

---

## ◈ GitHub Statistics

<p align="center">
  <img src="https://github-readme-stats-b5119.vercel.app/api?username=b5119&show_icons=true&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=58a6ff&icon_color=58a6ff&text_color=c9d1d9&include_all_commits=true&count_private=true&rank_icon=letters" width="495"/>
  &nbsp;
  <img src="https://github-readme-stats-b5119.vercel.app/api/top-langs/?username=b5119&layout=compact&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=58a6ff&text_color=c9d1d9&langs_count=6&hide=jupyter%20notebook" width="300"/>
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=b5119&theme=github-dark-blue&hide_border=true&background=0d1117&ring=58a6ff&fire=58a6ff&currStreakLabel=58a6ff&sideLabels=58a6ff&dates=c9d1d9" width="750"/>
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=b5119&bg_color=0d1117&color=58a6ff&line=58a6ff&point=c9d1d9&area=true&hide_border=true" width="750"/>
</p>

---

## ◈ Trophy Case

<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=b5119&theme=darkhub&no-frame=true&no-bg=true&margin-w=8&margin-h=8&column=7&title=Commits,PullRequest,Repositories,Stars,Followers,Experience,MultipleLang" alt="GitHub Trophies"/>
</p>

---

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

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&duration=2600&pause=750&color=58A6FF&center=true&vCenter=true&width=860&height=50&lines=%E2%9C%85+Application+Builder+%E2%80%94+shipped+systems+that+run;%E2%9C%85+Backend+Architect+%E2%80%94+service+boundaries+%26+API+discipline;%F0%9F%94%B5+Distributed+Systems+Engineer+%E2%80%94+consistency%2C+fault+tolerance+%5Bnow%5D;%F0%9F%8E%AF+Systems+Architect+%E2%80%94+design+the+structures%2C+not+just+the+apps" alt="Roadmap"/>
</p>

```mermaid
%%{init: {'theme':'dark', 'themeVariables': {'primaryColor':'#0d1117','primaryBorderColor':'#58a6ff','lineColor':'#58a6ff','primaryTextColor':'#c9d1d9','fontFamily':'Fira Code, monospace'}}}%%
flowchart LR
    A([✅ Application Builder<br/><i>multi-API dashboards</i>]):::done ==> B([✅ Backend Architect<br/><i>SigTrace · FastAPI</i>]):::done
    B ==> C([🔵 Distributed Systems Engineer<br/><b>Nexus · gRPC · FUSE</b><br/>· you are here ·]):::now
    C -.-> D([🎯 Systems Architect<br/><i>the horizon</i>]):::goal

    classDef done fill:#0d1117,stroke:#2ea043,color:#7ee787,stroke-width:2px;
    classDef now fill:#0b2545,stroke:#58a6ff,color:#58a6ff,stroke-width:3px;
    classDef goal fill:#0d1117,stroke:#bc8cff,color:#bc8cff,stroke-width:2px,stroke-dasharray:4 3;
```

<div align="center">

| Phase | Status | Driving work | Progress |
|:--|:--:|:--|:--|
| **Application Builder** | ✅ Done | Multi-API Flask dashboards | <img src="https://geps.dev/progress/100?successColor=2ea043" height="14"/> |
| **Backend Architect** | ✅ Done | SigTrace · FastAPI service layer | <img src="https://geps.dev/progress/100?successColor=2ea043" height="14"/> |
| **Distributed Systems Engineer** | 🔵 In progress | **Nexus** · gRPC · FUSE · device mesh | <img src="https://geps.dev/progress/35?successColor=58a6ff&warningColor=58a6ff&dangerColor=58a6ff" height="14"/> |
| **Systems Architect** | 🎯 Horizon | Designing the structures themselves | <img src="https://geps.dev/progress/10?successColor=bc8cff&warningColor=bc8cff&dangerColor=bc8cff" height="14"/> |

</div>

Not just code that runs. **Systems that endure.**

---

## ◈ Let's Connect

📧 **Email:** bwalyafrank61@gmail.com  
💼 **LinkedIn:** [Frank Bwalya](https://www.linkedin.com/in/frank-bwalya-64b124275)

---

## ◈ The Quote I Keep Coming Back To

> *"Knowledge is a paradox. The more we understand, the more we realize the vastness of our ignorance."*
>
> **— Viktor, Arcane**

That isn't discouragement. It's the only honest description of what engineering actually is — a permanent state of knowing enough to understand how much remains. The engineers worth learning from aren't the ones who know the most. They're the ones who've stayed long enough to understand *how much they don't know* — and kept building anyway.

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer"/>
</p>

<p align="center">
  <img src="https://img.shields.io/github/followers/b5119?label=Followers&style=social"/>
  &nbsp;
  <img src="https://img.shields.io/github/stars/b5119?label=Stars&style=social"/>
</p>

<p align="center">
  <sub>Last updated: 2026 · Lusaka, Zambia · Built with deliberate intent, not just enthusiasm ☕</sub>
</p>
