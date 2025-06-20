# 📈 CAPM Financial Analysis Web App

A lightweight web application that uses the **Capital Asset Pricing Model (CAPM)** to analyze stock performance, assess risk, and calculate expected returns. Built with Python and Streamlit, it enables interactive financial exploration using real-time market data.

---

## 🚀 Overview

This project demonstrates a simple yet powerful financial analytics tool. It allows users to:
- Select and analyze S&P 500 stocks
- Calculate expected returns using CAPM
- Visualize normalized prices and volatility
- Interpret beta values to assess investment risk

The app is fully interactive and runs locally using Streamlit. It's ideal for finance students, analysts, or anyone curious about how risk relates to return in the stock market.

---

## ⚙️ Tech Stack

| Component         | Description                                      |
|------------------|--------------------------------------------------|
| Python            | Core programming language                       |
| Streamlit         | Frontend framework for interactive UI           |
| Pandas & NumPy    | Data manipulation and calculations              |
| yfinance          | Stock data extraction from Yahoo Finance        |
| Plotly            | Visualizations                                  |

---

## 🧠 Core Concepts

### Capital Asset Pricing Model (CAPM)

CAPM describes the relationship between **risk** and **expected return** for a security. The formula is:

```
Expected Return = Risk-Free Rate + Beta * (Market Return - Risk-Free Rate)
```

- **Risk-Free Rate**: Typically the 10-year Treasury yield
- **Market Return**: Average return of the overall market (e.g., S&P 500)
- **Beta**: A measure of a stock's volatility relative to the market

### Beta Interpretation

| Beta Value | Meaning                        |
|------------|--------------------------------|
| 0          | No market sensitivity          |
| < 1        | Less volatile than the market  |
| 1          | Moves with the market          |
| > 1        | More volatile than the market  |
| < 0        | Moves opposite to the market   |

---

## 🛠️ How It Works

### 1. Application Setup
- Two main Python scripts:  
  `CAPM_Returns.py` – Main app logic  
  `capm_functions.py` – Helper functions
- Libraries like `yfinance`, `pandas_datareader`, and `datetime` are used for fetching and processing data.

### 2. Data Handling
- User selects 2 to 4 S&P 500 stock tickers
- The app pulls price history and computes:
  - Normalized prices
  - Daily returns
  - Beta and expected return using CAPM

### 3. Visual Output
- Interactive line charts of stock performance
- Tables of calculated metrics (Beta & Expected Return)

---

## ▶️ How to Run

Make sure you have Python and Streamlit installed:

```bash
pip install -r requirements.txt
```

Then launch the app using:

```bash
streamlit run CAPM_Returns.py
```

---

## 📊 Key Features

- ✅ Real-time data from Yahoo Finance
- ✅ Clean, interactive UI with no front-end coding
- ✅ Quick comparison of multiple stock performances
- ✅ CAPM-based return prediction with risk analysis
- ✅ Supports exploratory financial modeling for beginners

---

## 📂 Repository Structure

```
📁 CAPM-WebApp/
├── CAPM_Returns.py           # Main app script
├── capm_functions.py         # Helper functions for data & CAPM
├── requirements.txt          # Dependencies
├── README.md                 # Documentation
```

---

## 📌 Use Cases

- Finance or economics students practicing investment modeling
- Analysts comparing stock risk vs return
- Educators introducing CAPM concepts in a visual way

---

## 🧾 License

This project is open-source and free to use under the MIT License.