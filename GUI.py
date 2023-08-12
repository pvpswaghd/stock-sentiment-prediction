import streamlit as st
from datetime import datetime
import pandas as pd
import plotly.graph_objects as go

# if we have more than one test data(TSLA), we can read_excel files here and set it to be'stockData' below

#stockData = pd.read_excel("./Testing Data/TSLA.xlsx")

# Build of the SIDEBAR
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

st.sidebar.header("Stock Trend Prediction")

st.sidebar.subheader("Feature Selections")
stockName = st.sidebar.selectbox(
    "Options", ["TSLA", "AAPL", "META", "GOOG", "NDAQ", "SPY"]
)

st.sidebar.subheader("Prediction Methods")
predictMethod = st.sidebar.multiselect("Methods", ["Media Forcast", "Market Forcast"])

st.sidebar.subheader("Date")
dateObt = st.sidebar.date_input(
    "Select a date", datetime.strptime("2022-12-30", "%Y-%m-%d").date()
)  # EDIT THE DATE IF WE HAVE A MORE UPDATE DATA, ELSE THIS IS THE LATEST
dateStr = dateObt.strftime("%Y-%m-%d")


st.sidebar.subheader("Duration")
duration = st.sidebar.slider("Number of days", 30, 80, 50)

# PARAMETERS FOR METRICS

if ("Market Forcast" in predictMethod) and ("Media Forcast" in predictMethod):
    method = "Blend - Sentiment Volatility"
    stockData = pd.read_excel("./resultant_data/sentiment_volatility.xlsx")

elif predictMethod == ["Media Forcast"]:
    method = "Media - Sentiment"
    stockData = pd.read_excel("./resultant_data/sentiment.xlsx")

elif predictMethod == ["Market Forcast"]:
    method = "Market - Pure Date"
    stockData = pd.read_excel("./resultant_data/pure_data.xlsx")
else:
    method = "Blend - Sentiment Volatility"
    stockData = pd.read_excel("./resultant_data/sentiment_volatility.xlsx")

currIndex = stockData.loc[stockData["Date"] == dateStr].index[0]
yestIndex = currIndex - 1 if (currIndex > 0) else currIndex

predictCurrPrice = round(stockData.loc[currIndex]['Open_change'], 2)
actualCurrPrice = round(stockData.loc[currIndex]["Prediction"], 2)

diff1 = round(predictCurrPrice - round(stockData.loc[yestIndex]['Open_change'], 2), 2)
diff2 = round(
    actualCurrPrice - round(stockData.loc[yestIndex]["Prediction"], 2), 2
)


st.header(str(stockName) + " - " + "Stock Market Prediction")
col1, col2, col3 = st.columns(3)
col1.metric("Date", dateStr, "")
col2.metric("Predicted Price (USD)", "$" + str(predictCurrPrice), diff1)
col3.metric("Actual Price (USD)", "$" + str(actualCurrPrice), diff2)

# BELOW FOR THE PLOT

stockDataUpdated = stockData.iloc[currIndex - duration : currIndex]

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=stockDataUpdated["Date"],
        y=stockDataUpdated["Prediction"],
        line=dict(color="blue"),
        name="Actual Data",
    )
)
fig.add_trace(
    go.Scatter(
        x=stockDataUpdated["Date"],
        y=stockDataUpdated['Open_change'],
        line=dict(color="red"),
        name=str(method),
    )
)
st.plotly_chart(fig)