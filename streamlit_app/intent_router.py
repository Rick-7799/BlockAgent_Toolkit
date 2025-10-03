from dataclasses import dataclass
from typing import Optional

@dataclass
class Intent:
    action: str
    chain: Optional[str] = None
    address: Optional[str] = None
    value: Optional[int] = None
    args: Optional[list] = None

def parse_prompt(text: str) -> Intent:
    t = text.lower().strip()

    # chain detection
    chain = None
    for c in ["celo", "aurora", "harmony"]:
        if c in t:
            chain = c
            break

    # basic intents
    if "new wallet" in t or "create wallet" in t:
        return Intent(action="NEW_WALLET", chain=chain)

    if "balance" in t or "check my money" in t:
        # try to find an address in the text (very naive)
        addr = None
        for w in t.split():
            if w.startswith("0x") and len(w) > 20:
                addr = w
                break
        return Intent(action="GET_BALANCE", chain=chain, address=addr)

    if "deploy" in t and "storage" in t:
        return Intent(action="DEPLOY_SIMPLE_STORAGE", chain=chain)

    if "set value" in t or "set storage" in t:
        # extract number
        import re
        m = re.search(r'(\d+)', t)
        val = int(m.group(1)) if m else 0
        return Intent(action="SET_STORAGE", chain=chain, value=val)

    if "read" in t or "get value" in t:
        return Intent(action="READ_STORAGE", chain=chain)

    return Intent(action="UNKNOWN", chain=chain)
