<!-- Header -->
<p align="center">
  <img src="./assets/doom-banner.svg?v=3" alt="Frank Bwalya — Systems Thinker, Backend & Distributed Systems" width="900"/>
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&duration=3000&pause=900&color=3DDC84&background=FFFFFF00&center=true&vCenter=true&multiline=true&width=900&height=110&lines=Building+Nexus+%E2%80%94+a+personal+device+mesh+in+Rust;Making+public+money+provable+%E2%80%94+CDF+SigTrace;Go+backends+%C2%B7+Rust+systems+%C2%B7+Solidity+contracts" alt="Currently building: Nexus, a personal device mesh in Rust; CDF SigTrace, a blockchain-anchored public-spending audit system"/>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/frank-bwalya-64b124275"><img src="./assets/badges/linkedin.svg" alt="LinkedIn"/></a>
  <a href="mailto:bwalyafrank61@gmail.com"><img src="./assets/badges/email.svg" alt="Email"/></a>
</p>

<p align="center"><img src="./assets/doom-divider.svg?v=2" width="860" alt=""/></p>

I'm a final-year software engineering student in Lusaka who builds **backend and distributed systems** that have to hold up under real constraints: patchy connectivity, privacy law, money that must reconcile. I write in **Rust, Go and Python**, document design decisions as I make them, and gate every change with tests and CI.

<div align="center">
<table>
<tr><td nowrap>🏆 <b>Award</b></td><td>1st place, 2026 ZAMREN Student Hackathon (ZedLedger)</td></tr>
<tr><td nowrap>🔧 <b>Shipped</b></td><td>100+ merged pull requests across 11 repositories, including a Flutter internship shipping offline-first features to production</td></tr>
<tr><td nowrap>🎓 <b>Studying</b></td><td>BSc Software Engineering, ZCAS University (final year)</td></tr>
<tr><td nowrap>🔎 <b>Open to</b></td><td>Backend and distributed-systems internships; open-source collaboration</td></tr>
</table>
</div>

<p align="center"><img src="./assets/doom-divider.svg?v=2" width="860" alt=""/></p>

## ◈ Featured Projects

### Nexus — personal device mesh *(active)*
Mount a paired device's files as a real filesystem, stream its screen and migrate app state, all over an mTLS-encrypted, code-paired connection. Built from scratch in Rust.

- **Lazy FUSE filesystem** with vector-clock conflict detection: concurrent edits keep both versions, never silently lose data
- **Device pairing** with a 6-digit code and per-device certificates; proven on a real Android phone → Linux laptop mount, byte-exact
- **Screen streaming** (H.264 over gRPC) and an app-state **migration SDK** with three conflict policies
- **Engineering discipline:** 100+ tests, CI on every PR (build, test, fmt, clippy), branch-protected `main`, 17 ADRs recording each real constraint hit

`Rust` · `Tokio` · `gRPC/tonic` · `FUSE` · `mTLS` · `Android (cargo-ndk)` — [Repository](https://github.com/b5119/nexus)

### CDF SigTrace & CDF Pulse — final-year project
A blockchain-anchored way to check Zambia's public spending. **SigTrace** makes contract integrity verifiable by anyone; **Pulse** lets community monitors confirm project delivery with GPS-tagged photos, offline-first; a monitor flags payments with no confirmed completion.

- **Eight readable integrity checks** over real ZPPA open-contracting data, with SHA-256 anchoring of each signed contract
- **Privacy by architecture:** personal data stays off-chain; outputs are signals for human review, never findings of wrongdoing
- **Honest scope:** Fabric and Polygon are simulated in the prototype, and demonstration data is labelled as such

`Python` · `FastAPI` · `PostgreSQL` · `Solidity` · `React` — 🌐 [Live demo](https://frontend-public-app.vercel.app) · 🔒 source private, walkthrough on request

### 🏆 ZedLedger — national digital ID platform *(1st place, ZAMREN 2026)*
<p align="center">
  <img src="./assets/zedledger.svg" alt="ZedLedger — Zambia eNID Platform. 1st prize, Zambia Digital ID category, 2026 ZAMREN Student Hackathon." width="760"/>
</p>

A team of four built citizen registration, eNID issuance and civil registration (births and deaths) with blockchain-anchored certificates under hackathon conditions. I was **backend lead** for the identity, mobile-money (GSB / ISO 8583), immigration, blockchain and API-gateway services: seven microservices behind one JWT-validating gateway, with isolated PostgreSQL schemas per domain, aligned to the Data Protection Act No. 3 of 2021.

`Next.js` · `FastAPI` · `Hyperledger Fabric` · `PostgreSQL` · `Docker` — 🔒 private, walkthrough on request

### More work
| Project | What it is |
|:--|:--|
| [ChainBa](https://github.com/b5119/chainba) | Decentralised Chilimba (rotating savings) on Ethereum: Solidity contracts, 23 Hardhat tests, React dApp |
| [GPA Tracker](https://github.com/b5119/gpa_tracker) | Flutter app with offline-first storage, predictive GPA modelling and career-sector mapping |
| [Flask API Dashboard](https://github.com/b5119/flask-api-dashboard) | Multi-API dashboard with a service layer and blueprints |
| [ext4 recovery case study](https://github.com/b5119/ext4-partition-recovery-case-study) | Recovering a filesystem after power loss mid-partition-move; zero data lost |

<p align="center"><img src="./assets/doom-divider.svg?v=2" width="860" alt=""/></p>

## ◈ Technical Stack

<div align="center">
<table>
<tr><td align="left" nowrap><b>Languages</b><br/><sub>what I ship in</sub></td><td align="left"><img src="https://skillicons.dev/icons?i=rust,go,python,ts,js,dart,kotlin,solidity&theme=dark" alt="Rust, Go, Python, TypeScript, JavaScript, Dart, Kotlin, Solidity"/><br/><img src="https://skillicons.dev/icons?i=java,cs,php,bash,sql&theme=dark" alt="Java, C#, PHP, Bash, SQL"/></td></tr>
<tr><td align="left" nowrap><b>Backend & APIs</b><br/><sub>services and contracts</sub></td><td align="left"><img src="https://skillicons.dev/icons?i=fastapi,flask,laravel,nodejs,dotnet,swagger&theme=dark" alt="FastAPI, Flask, Laravel, Node.js, .NET, Swagger"/><br/><img src="./assets/badges/go-chi.svg" alt="go-chi"/> <img src="./assets/badges/openapi.svg" alt="openapi"/> <img src="./assets/badges/grpc.svg" alt="grpc"/> <img src="./assets/badges/protobuf.svg" alt="protobuf"/></td></tr>
<tr><td align="left" nowrap><b>Systems</b><br/><sub>low-level and distributed</sub></td><td align="left"><img src="./assets/badges/tokio.svg" alt="tokio"/> <img src="./assets/badges/fuse.svg" alt="fuse"/> <img src="./assets/badges/grpc.svg" alt="grpc"/> <img src="./assets/badges/protobuf.svg" alt="protobuf"/> <img src="./assets/badges/tailscale.svg" alt="tailscale"/> <img src="./assets/badges/ssh.svg" alt="ssh"/></td></tr>
<tr><td align="left" nowrap><b>Blockchain</b><br/><sub>contracts and anchoring</sub></td><td align="left"><img src="https://skillicons.dev/icons?i=solidity,hardhat&theme=dark" alt="Solidity, Hardhat"/><br/><img src="./assets/badges/hyperledger-fabric.svg" alt="hyperledger-fabric"/> <img src="./assets/badges/polygon.svg" alt="polygon"/> <img src="./assets/badges/ipfs.svg" alt="ipfs"/></td></tr>
<tr><td align="left" nowrap><b>Frontend & Mobile</b><br/><sub>web and cross-platform</sub></td><td align="left"><img src="https://skillicons.dev/icons?i=flutter,dart,react,angular,kotlin,tailwind,bootstrap,vite&theme=dark" alt="Flutter, Dart, React, Angular, Kotlin, Tailwind, Bootstrap, Vite"/></td></tr>
<tr><td align="left" nowrap><b>Data</b><br/><sub>storage</sub></td><td align="left"><img src="https://skillicons.dev/icons?i=postgres,sqlite,mongodb,firebase,supabase&theme=dark" alt="PostgreSQL, SQLite, MongoDB, Firebase, Supabase"/></td></tr>
<tr><td align="left" nowrap><b>Infra & Tooling</b><br/><sub>delivery and workflow</sub></td><td align="left"><img src="https://skillicons.dev/icons?i=docker,aws,githubactions,linux,ubuntu,git,neovim,vscode&theme=dark" alt="Docker, AWS, GitHub Actions, Linux, Ubuntu, Git, Neovim, VS Code"/></td></tr>
<tr><td align="left" nowrap><b>Integrating in 2026</b><br/><sub>actively learning</sub></td><td align="left"><img src="https://skillicons.dev/icons?i=kubernetes,kafka,graphql,redis&theme=dark" alt="Kubernetes, Kafka, GraphQL, Redis"/></td></tr>
</table>
</div>

<p align="center"><img src="./assets/doom-divider.svg?v=2" width="860" alt=""/></p>

## ◈ GitHub Activity

<p align="center">
  <img src="https://github-readme-stats-b5119.vercel.app/api?username=b5119&show_icons=true&theme=github_dark&hide_border=true&border_color=1f3a2b&bg_color=0b1410&title_color=3ddc84&icon_color=c9a227&text_color=cfe8d8&include_all_commits=true&count_private=true&rank_icon=letters" width="440" alt="GitHub stats"/>
</p>

<p align="center">
  <img src="./assets/top-langs.svg?v=2" alt="Most used languages, weighted by commits across all repositories I contribute to" width="380"/>
</p>

<p align="center"><img src="./assets/doom-divider.svg?v=2" width="860" alt=""/></p>

## ◈ What I'm Looking For

- **Backend or distributed-systems internships** where I can work on real production constraints
- **Open-source backend contributions:** meaningful pull requests, not surface-level fixes
- **Blockchain infrastructure projects** with a genuine use case

I'm deepening backend architecture, distributed-systems theory (consistency, fault tolerance, replication) and smart-contract security.

📧 [bwalyafrank61@gmail.com](mailto:bwalyafrank61@gmail.com) · 💼 [LinkedIn](https://www.linkedin.com/in/frank-bwalya-64b124275)

<p align="center"><sub>Lusaka, Zambia · Updated November 2026</sub></p>
