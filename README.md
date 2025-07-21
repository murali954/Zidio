📈 Stock Forecasting with ARIMA + 🤖 Chatbot
This Streamlit web app forecasts stock prices using the ARIMA time series model and features an AI-powered chatbot that answers questions about future trends. Users can select a company, view historical prices, forecast future prices, and evaluate model accuracy.

🚀 Features
📊 Interactive selection of companies from uploaded stock data

📉 ARIMA-based time series forecasting for Close prices

📏 Evaluation metrics: MAE, RMSE, MAPE

📋 Forecast vs Actual table

📈 Plot showing actual vs predicted prices

💬 Cohere-powered chatbot that answers forecast-related questions

🧾 Sidebar with dataset preview and branding image

🧾 Dataset Format
The uploaded stock_data.csv must have at least the following columns:

Date (in YYYY-MM-DD format)

Company (company name)

Close (closing stock price)

Example:

Date	Company	Close
2023-01-01 AMD	3510.75
2023-01-02	MCD	3532.60
...	...	...

🛠 Tech Stack
Python

Streamlit

Pandas

Matplotlib

Statsmodels (ARIMA)

Scikit-learn

Cohere API

⚙️ How to Run
Clone the repository or copy the script.
Install dependencies:

pip install streamlit pandas matplotlib statsmodels scikit-learn cohere
Set your Cohere API key:
export COHERE_API_KEY=your_api_key_here
Place stock_data.csv and Untitled.jpeg in the root folder.

Run the app:
streamlit run app.py

📌 Notes
The ARIMA model is currently set with order (5,1,0) — you can tune it for better results.
The chatbot uses Cohere's generate endpoint and works best with concise, specific queries.

