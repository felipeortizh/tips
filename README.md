#Waiter's Tip Prediction

Predict customer tips in real‑time using a simple multilinear regression model served with Streamlit.

📝 Project Overview

This web app lets restaurant staff (or anyone curious!) estimate the gratuity a party is likely to leave based on:

Total bill

Party size

Day & time of the meal

Gender of the bill payer

Whether the table was smoking

Behind the scenes it trains a LinearRegression model from scikit‑learn on the classic tips data set, then serves interactive predictions and exploratory data analysis (EDA) charts built with Plotly.

⚡ Quickstart

# 1. Clone the repo
$ git clone https://github.com/felipeortizh/tips.git
$ cd tips

# 2. Create and activate a virtual environment (optional but recommended)
$ python -m venv .venv
$ source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install Python dependencies
$ pip install -r requirements.txt

# 4. Launch the app locally
$ streamlit run tips.py

Open the URL shown in your terminal (usually http://localhost:8501) and start experimenting! 🎉

Tip: Use the sidebar sliders & dropdowns to try different scenarios; all charts update instantly.

📂 Repository structure

├── tips.py          # Streamlit application
├── tips.csv         # Training data (sourced from Kaggle ‑ see below)
├── requirements.txt # Python package versions
├── Procfile         # Heroku entry‑point
├── setup.sh         # Minimal Streamlit config for Heroku
└── README.md        # You are here

📊 Data source

The app ships with the tidy `` data set originally shared by Joseph Redmon on Kaggle ▶︎ https://www.kaggle.com/datasets/jsphyg/tipping

🧠 Model details

Algorithm: Ordinary Least Squares (OLS) multilinear regression

Training / test split: 80 % / 20 %

Features: total_bill, sex, smoker, day, time, size

Target: tip

All categorical variables are mapped to integers inside tips.py before model fitting.

☁️ One‑click deploy to Heroku

This repo already contains a Procfile and a tiny setup.sh, so you can deploy in minutes:

Push the code to a new Heroku app linked to your GitHub account.

Set the buildpack to heroku/python.

Enable automatic deploys or deploy manually.

Heroku will install the dependencies, run the Streamlit server on the $PORT Heroku assigns, and your prediction app will be live!

🤝 Contributing

Found a bug or have an idea for a cool new feature? Fork the repo and open a pull request—issues & PRs are welcome.

📜 License

This project is released under the MIT License.  See LICENSE for details (or add one if it’s missing).

🙋‍♂️ Author

Felipe Ortiz  •  fortiz.huerta@gmail.com  •  @felipeortizh

Made with ☕, 🐍 and ❤️.
