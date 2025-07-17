# Aave Wallet Credit Scorer

This repository provides a transparent, end‑to‑end pipeline to assign a **0–1000 credit score** to each Aave V2 user wallet based solely on on‑chain transaction behavior. High scores indicate reliable, responsible usage; low scores flag risky or exploit‑style activity.

---

## 📁 Repository Structure

├── README.md ← This overview
├── requirements.txt ← Python dependencies
├── analysis.md ← Post‑scoring insights + histogram
├── credit_score_hist.png ← Distribution plot
├── notebooks/
│ └── credit_score_assignment.ipynb ← Colab notebook with full pipeline
└── src/
├── load_data.py ← JSON loader & normalizer
├── features.py ← Feature engineering
├── model.py ← Isolation Forest training & scoring
└── score_wallets.py ← CLI script tying it all together


---

## Getting Started

### 1. Clone the repo


git clone https://github.com/abhigyanpal1/aave-credit-scorer.git
cd aave-credit-scorer

### 2. Install dependencies
python3 -m venv venv
source venv/bin/activate      # on Windows: .\venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt


### Usage
A) Run in Google Colab (recommended)
Open notebooks/credit_score_assignment.ipynb in Colab.

Upload your JSON file (e.g. user-wallet-transactions.json) or mount Drive.

Run all cells—this will:

Stream‑load the JSON

Engineer features

Train an Isolation Forest

Score each wallet

Save scores.csv and plot the distribution

Save a copy back to GitHub via File → Save a copy in GitHub… to keep your notebook in sync.

### Analysis
After scoring, view the histogram and key findings in analysis.md, or directly open credit_score_hist.png.

### Contributing
Fork the repo

Create a branch (git checkout -b feature/XYZ)

Make your changes & add tests

Commit (git commit -m "Add XYZ feature")

Push & open a Pull Request




