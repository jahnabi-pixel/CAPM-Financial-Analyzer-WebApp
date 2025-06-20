# CAPM_Returns.py (Enhanced & Commented Version)

import streamlit as st
import pandas as pd
import yfinance as yf
import pandas_datareader.data as web
import datetime
import capm_functions

# Set Streamlit page configuration
st.set_page_config(
    page_title="CAPM Financial Analysis",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add a colorful title
st.markdown("""
    <h1 style='text-align: center; color: #3366cc;'>
        📈 Capital Asset Pricing Model (CAPM) Analysis
    </h1>
    <hr style='border: 1px solid #ddd;'>
""", unsafe_allow_html=True)

# --- User Inputs ---
col1, col2 = st.columns([1, 1])

with col1:
    stock_list = st.multiselect(
        "Select up to 4 stocks:",
        ('TSLA', 'AAPL', 'NFLX', 'MSFT', 'MGM', 'AMZN', 'NVDA', 'GOOGL'),
        ['TSLA', 'AAPL', 'AMZN', 'GOOGL']
    )

with col2:
    year = st.number_input("Choose number of years to analyze:", 1, 10)

try:
    # --- Fetching Market Data ---
    end = datetime.date.today()
    start = datetime.date(end.year - year, end.month, end.day)

    SP500 = web.DataReader(['sp500'], 'fred', start, end)

    # Download stock data using yfinance
    stocks_df = pd.DataFrame()
    for stock in stock_list:
        data = yf.download(stock, period=f'{year}y')
        stocks_df[stock] = data['Close']

    # Prepare and merge data
    stocks_df.reset_index(inplace=True)
    SP500.reset_index(inplace=True)
    SP500.columns = ['Date', 'sp500']

    stocks_df['Date'] = pd.to_datetime(stocks_df['Date'])
    stocks_df = pd.merge(stocks_df, SP500, on='Date', how='inner')

    # --- Display Raw Data ---
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("### 🔢 Head of Data")
        st.dataframe(stocks_df.head(), use_container_width=True)
    with col2:
        st.markdown("### 🔢 Tail of Data")
        st.dataframe(stocks_df.tail(), use_container_width=True)

    # --- Price Visualizations ---
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("### 📈 Raw Stock Prices")
        st.plotly_chart(capm_functions.interactive_plot(stocks_df), use_container_width=True)
    with col2:
        st.markdown("### 📊 Normalized Prices")
        normalized_df = capm_functions.normalize(stocks_df)
        st.plotly_chart(capm_functions.interactive_plot(normalized_df), use_container_width=True)

    # --- Daily Returns & Beta Calculation ---
    stocks_daily_return = capm_functions.daily_return(stocks_df)

    beta, alpha = {}, {}
    for stock in stocks_daily_return.columns:
        if stock not in ['Date', 'sp500']:
            b, a = capm_functions.calculate_beta(stocks_daily_return, stock)
            beta[stock] = b
            alpha[stock] = a

    # --- Display Beta Values ---
    beta_df = pd.DataFrame({
        'Stock': list(beta.keys()),
        'Beta Value': [round(val, 2) for val in beta.values()]
    })
    with col1:
        st.markdown('### 📊 Beta Values')
        st.dataframe(beta_df, use_container_width=True)

    # --- CAPM Return Calculation ---
    rf = 0  # Risk-free rate
    rm = stocks_daily_return['sp500'].mean() * 252  # Market return annualized

    return_value = [round(rf + beta[stock] * (rm - rf), 2) for stock in stock_list]
    return_df = pd.DataFrame({
        'Stock': stock_list,
        'Expected Return (CAPM)': return_value
    })

    with col2:
        st.markdown('### 📉 Expected Returns via CAPM')
        st.dataframe(return_df, use_container_width=True)

except Exception as e:
    st.error("Please select valid inputs or check your internet connection.")
    st.exception(e)
