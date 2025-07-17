import argparse
import os
from load_data import load_raw_json
from features  import engineer_features
from model     import train_model, score_wallets

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--input',  required=True, help='Path to raw JSON')
    p.add_argument('--output', required=True, help='CSV output path')
    args = p.parse_args()

    df      = load_raw_json(args.input)
    feats   = engineer_features(df)
    scaler, iso = train_model(feats)
    scored  = score_wallets(feats, scaler, iso)

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    scored.to_csv(args.output, index=False)
    print(f"✅ Scores written to {args.output}")

if __name__ == '__main__':
    main()
