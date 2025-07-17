import pandas as pd

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    now = df['timestamp'].max()
    feats = []
    for wallet, sub in df.groupby('userWallet'):
        counts = sub['action'].value_counts().to_dict()
        sums   = sub.groupby('action')['amount'].sum().to_dict()
        borrow = counts.get('borrow', 0)
        repay  = counts.get('repay', 0)
        feats.append({
            'userWallet':      wallet,
            'n_deposits':      counts.get('deposit', 0),
            'total_deposit':   sums.get('deposit', 0.0),
            'n_borrows':       borrow,
            'total_borrow':    sums.get('borrow', 0.0),
            'repay_ratio':     repay/borrow if borrow>0 else 0.0,
            'n_liquidations':  counts.get('liquidationcall', 0),
            'distinct_assets': sub['assetSymbol'].nunique(),
            'days_since_last': (now - sub['timestamp'].max()).days,
        })
    return pd.DataFrame(feats).fillna(0)
