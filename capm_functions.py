# capm_functions.py (Enhanced with Comments and Visual Tweaks)

import plotly.express as px
import numpy as np
import pandas as pd

# Function to plot interactive plotly chart with custom theme

def interactive_plot(df):
    fig = px.line()
    for col in df.columns[1:]:  # Skip 'Date' column
        fig.add_scatter(x=df['Date'], y=df[col], name=col)

    fig.update_layout(
        title="Stock Price Over Time",
        title_font=dict(size=20, color="#3366cc"),
        template="plotly_white",
        width=500,
        margin=dict(l=30, r=30, t=30, b=30),
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1,
            font=dict(size=12)
        ),
        hovermode="x unified"
    )
    return fig

# Function to normalize stock prices based on the first value
def normalize(df_2):
    df = df_2.copy()
    for col in df.columns[1:]:
        df[col] = df[col] / df[col][0]
    return df

# Function to compute daily returns in percentage
def daily_return(df):
    df_daily_return = df.copy()
    for col in df.columns[1:]:
        df_daily_return[col] = df[col].pct_change().fillna(0) * 100
    return df_daily_return

# Function to calculate Beta and Alpha for a stock relative to market

def calculate_beta(stocks_daily_return, stock):
    # Estimate Beta and Alpha using linear regression
    x = stocks_daily_return['sp500']
    y = stocks_daily_return[stock]
    b, a = np.polyfit(x, y, 1)  # 1 = linear regression
    return b, a
