import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import MinMaxScaler

def train_model(feat_df):
    X = feat_df.drop('userWallet', axis=1).values
    scaler = MinMaxScaler().fit(X)
    iso    = IsolationForest(contamination=0.05, random_state=42)\
                .fit(scaler.transform(X))
    return scaler, iso

def score_wallets(feat_df, scaler, model):
    X = feat_df.drop('userWallet', axis=1).values
    Xs = scaler.transform(X)
    raw = -model.decision_function(Xs)
    mn, mx = raw.min(), raw.max()
    norm   = (raw - mn) / (mx - mn + 1e-9)
    scores = (norm * 1000).astype(int)
    out    = feat_df[['userWallet']].copy()
    out['score'] = scores
    return out
