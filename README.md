# BlockAgent Toolkit

AI-powered toolkit that makes secure blockchain interactions easy across EVM-compatible networks (Celo, Aurora, Harmony).  
Tech stack: **Web3.js** (on Node), **REST API (Express)**, **Streamlit** frontend.  
Targets 50+ dApps style use-cases and 1,000+ tx/month scale with simple, safe flows.

## Project Layout
```
BlockAgent_Toolkit/
├─ backend/                 # Node.js REST API (web3.js)
│  ├─ index.js
│  ├─ package.json
│  ├─ .env.example
│  └─ README.md
├─ contracts/               # Hardhat project + sample contract
│  ├─ contracts/SimpleStorage.sol
│  ├─ scripts/deploy.js
│  ├─ hardhat.config.js
│  ├─ package.json
│  └─ README.md
├─ streamlit_app/           # Streamlit "AI" UI (prompt → action router)
│  ├─ app.py
│  ├─ intent_router.py
│  ├─ requirements.txt
│  └─ .streamlit/config.toml
└─ README.md                # This file
```

## Quick Start (Like you're 5 😊)

### 0) Install the tools (one time)
- Install **Node.js 18+** from nodejs.org
- Install **Python 3.10+**
- Install **Git** (optional, just for your comfort)

### 1) Make your secret note (testnets only please)
Copy `backend/.env.example` to `backend/.env` and put your **testnet** RPCs + private key (fund a test account with testnet faucet coins only!)

```
CELO_RPC=https://alfajores-forno.celo-testnet.org
AURORA_RPC=https://testnet.aurora.dev
HARMONY_RPC=https://api.s0.b.hmny.io
PRIVATE_KEY=0xYOUR_TEST_PRIVATE_KEY_ONLY
DEFAULT_CHAIN=celo   # celo | aurora | harmony
```

### 2) Start the backend (the "robot helper")
```bash
cd backend
npm install
npm start
```
You should see: `Server listening on http://localhost:4000`

### 3) (Optional) Build the contract bundle
```bash
cd ../contracts
npm install
npx hardhat compile
# to deploy (testnet):
# npx hardhat run scripts/deploy.js --network celoTest
```

### 4) Start the Streamlit app (the "friendly face")
```bash
cd ../streamlit_app
pip install -r requirements.txt
streamlit run app.py
```
Your browser opens. Type simple requests like:
- "create a new wallet"
- "check my balance on celo"
- "deploy simple storage"
- "set value 42 on my storage"
- "call read on storage"

The app translates your words → API calls.

### 5) Safety
- **NEVER** use a real/private key with funds here.
- Use **testnets** only.
- Keep `.env` private (don't commit it).
- For production, use HSMs, managed wallets, or custodial services.

---

## What you get
- **web3.js + REST API** to sign/send transactions, deploy and call contracts.
- **Streamlit UI** that turns simple English-ish prompts into safe, limited actions.
- **Hardhat** project to compile/deploy a sample Solidity contract.

Enjoy!
