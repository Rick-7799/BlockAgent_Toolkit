# Backend (web3.js + Express)

Simple REST API for EVM chains (Celo, Aurora, Harmony). Uses a single test-only private key from `.env`.

## Endpoints
- `POST /wallet/new` → creates a brand-new wallet (address + privateKey) **in-memory only** (returns to caller; do not store server-side).
- `GET /balance?address=...&chain=...` → returns ETH/CELO ONE balance.
- `POST /tx/send` → send native token from server's signer to a destination.
- `POST /contract/deploy` → deploy SimpleStorage (or any ABI/bytecode given in body).
- `POST /contract/call` → call a read/write method on a contract (if write, it signs using server signer).

**Note**: This reference server is for **testnets** only. Do NOT use real funds or production secrets.
