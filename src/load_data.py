import json
import pandas as pd
from datetime import datetime

DECIMALS = {'USDC':6, 'USDT':6, 'DAI':18, 'WMATIC':18}

def load_raw_json(path: str) -> pd.DataFrame:
    with open(path, 'r') as f:
        data = json.load(f)
    rows = []
    for e in data:
        amt_raw = int(e['actionData']['amount'])
        dec    = DECIMALS.get(e['actionData']['assetSymbol'], 18)
        amt    = amt_raw / (10 ** dec)
        rows.append({
            'userWallet':    e['userWallet'],
            'action':        e['action'],
            'timestamp':     datetime.fromtimestamp(e['timestamp']),
            'assetSymbol':   e['actionData']['assetSymbol'],
            'amount':        amt,
            'assetPriceUSD': float(e['actionData']['assetPriceUSD']),
        })
    return pd.DataFrame(rows)
