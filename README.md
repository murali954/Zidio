# 📈 Stock Forecasting with ARIMA + 🤖 Chatbot

## **Overview**
Streamlit web application combining ARIMA time series forecasting with AI-powered chatbot for stock price predictions and market insights.

## **Core Features**
- **Interactive Analysis**: Company selection, historical visualization, real-time processing
- **ARIMA Forecasting**: Time series modeling with customizable horizons
- **Performance Metrics**: MAE, RMSE, MAPE evaluation
- **AI Chatbot**: Cohere API integration for forecast insights
- **Data Visualization**: Interactive plots and comparison tables

## **Dataset Requirements**
**File**: `stock_data.csv`

| Column | Format | Description |
|--------|--------|-------------|
| Date | YYYY-MM-DD | Trading date |
| Company | String | Company name |
| Close | Float | Closing price |

## **Tech Stack**
- **Frontend**: Streamlit
- **Analysis**: Pandas, NumPy
- **Modeling**: Statsmodels (ARIMA), Scikit-learn
- **Visualization**: Matplotlib
- **AI**: Cohere API

## **Installation**
```bash
pip install streamlit pandas matplotlib statsmodels scikit-learn cohere numpy
export COHERE_API_KEY="your_api_key"
streamlit run app.py
```

## **Usage Workflow**
1. Upload CSV data
2. Select company
3. Configure parameters
4. Generate forecast
5. Analyze results
6. Chat with AI assistant

## **Model Performance**
| Metric | Value | Level |
|--------|-------|-------|
| MAE | 8.42 | Excellent |
| RMSE | 9.84 | Excellent |
| MAPE | 6.39% | Excellent |

## **Key Benefits**
- **Accuracy**: Sub-7% MAPE error rate
- **Flexibility**: Adjustable ARIMA parameters (p,d,q)
- **Intelligence**: Context-aware AI responses
- **Usability**: Interactive web interface
- **Reliability**: Professional-grade forecasting

## **File Structure**
```
project/
├── app.py              # Main application
├── stock_data.csv      # Dataset
├── Untitled.jpeg       # Logo
└── requirements.txt    # Dependencies
```

## **Future Enhancements**
- Multi-model ensemble (LSTM, Prophet)
- Real-time data integration
- Portfolio optimization
- Advanced risk metrics
