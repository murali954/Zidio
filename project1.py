import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error
import cohere
import os

# Streamlit config
st.set_page_config(layout="wide")

# Load dataset
df = pd.read_csv("stock_data.csv")
df['Date'] = pd.to_datetime(df['Date'], utc=True).dt.tz_localize(None)
df.set_index('Date', inplace=True)

# --- SIDEBAR ---
st.sidebar.header("📊 Data Overview")
st.sidebar.dataframe(df.head(300), height=300)

# Sidebar image

# --- MAIN APP ---
st.title("📈 Stock Forecasting with ARIMA + 🤖 Chatbot")

# Two-column layout
col1, col2 = st.columns([3, 1])

with col1:
    # Company selection
    if 'Company' in df.columns:
        companies = df['Company'].unique()
        company = st.selectbox("Choose a company", companies)
        company_df = df[df['Company'] == company][['Close']]
    else:
        st.error("❌ 'Company' column not found in dataset.")
        st.stop()

    # Historical prices
    st.subheader("📊 Historical Stock Prices")
    st.line_chart(company_df)

    # ARIMA Forecasting
    st.subheader("🔮 ARIMA Forecasting")
    forecast_days = st.slider("Forecast days", 10, 100, 30)

    model = ARIMA(company_df, order=(5, 1, 0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=forecast_days)

    future_dates = pd.date_range(start=company_df.index[-1] + pd.Timedelta(days=1),
                                 periods=forecast_days)
    forecast_df = pd.DataFrame({'Forecast': forecast}, index=future_dates)

    # Evaluation
    st.subheader("📏 Evaluation Metrics")
    train = company_df[:-forecast_days]
    test = company_df[-forecast_days:]

    model = ARIMA(train, order=(5, 1, 0))
    model_fit = model.fit()
    preds = model_fit.forecast(steps=len(test))

    mae = mean_absolute_error(test, preds)
    rmse = np.sqrt(mean_squared_error(test, preds))
    mape = np.mean(np.abs((test.values - preds.values) / test.values)) * 100

    st.metric("MAE", f"{mae:.2f}")
    st.metric("RMSE", f"{rmse:.2f}")
    st.metric("MAPE (%)", f"{mape:.2f}")

    # Table: Actual vs Predicted
    st.subheader("📋 Forecast vs Actual Table")
    comparison_df = pd.DataFrame({
        "Actual": test.values.flatten(),
        "Predicted": preds.values.flatten()
    }, index=test.index)
    st.dataframe(comparison_df)

    # Chart: Actual vs Predicted
    st.subheader("📉 Actual vs Predicted Price Chart")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(test.index, test.values, label='Actual', color='blue', linewidth=2)
    ax.plot(test.index, preds, label='Predicted', color='orange', linestyle='--', linewidth=2)
    ax.set_title(f"{company} - Actual vs Predicted Prices", fontsize=14)
    ax.set_xlabel("Date")
    ax.set_ylabel("Stock Price")
    ax.legend()
    st.pyplot(fig)

with col2:
    st.subheader("💬 Chat with Forecast Assistant")
    question = st.text_input("Ask about forecast:")
    if question:
        co = cohere.Client(os.getenv("COHERE_API_KEY") or 'IDlfxdy11paDxht8zQKuLQZkR61dhaPRTwdNzkpF')
        prompt = f"""You are a stock forecasting assistant. The last {forecast_days} days' predicted closing prices for {company} are:\n\n{forecast_df.to_string()}\n\nNow answer this question:\n{question}"""
        response = co.generate(prompt=prompt, max_tokens=300)
        st.markdown(f"**Answer:** {response.generations[0].text.strip()}")
