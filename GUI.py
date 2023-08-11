import streamlit as st
from datetime import date, datetime, timedelta
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# if we have more than one test data(TSLA), we can read_excel files here and set it to be'stockData' below

stockData = pd.read_excel('./Testing Data/TSLA.xlsx')

# Build of the SIDEBAR
st.set_page_config(layout= 'wide', initial_sidebar_state='expanded')

st.sidebar.header("Stock Trend Prediction")

st.sidebar.subheader('Feature Selections')
stockName = st.sidebar.selectbox('Options', ["TSLA", "AAPL", "META", "GOOG", "NDAQ", "SPY"])

st.sidebar.subheader('Prediction Methods')
predictMethod = st.sidebar.multiselect('Methods', ["Media Forcast", "Market Forcast"])

st.sidebar.subheader('Date')
dateObt = st.sidebar.date_input("Select a date", datetime.strptime("2020-02-03", "%Y-%m-%d").date()) # EDIT THE DATE IF WE HAVE A MORE UPDATE DATA, ELSE THIS IS THE LATEST
dateStr = dateObt.strftime("%Y-%m-%d")

st.sidebar.subheader('Duration')
duration = st.sidebar.slider('Number of days', 30, 365, 150)

# PARAMETERS FOR METRICS

if (("Market Forcast" in predictMethod) and ("Media Forcast" in predictMethod)):
    method = "Open(Act as Blend)"

elif (predictMethod == ["Media Forcast"]):
    method = "High(Act as Media)"

elif (predictMethod == ["Market Forcast"]):
    method = "Low(Act as Market)"
else:
    method = "Open(Act as Blend)"

currIndex = stockData.loc[stockData['Date'] == dateStr].index[0]
yestIndex = currIndex - 1 if (currIndex > 0) else currIndex

predictCurrPrice = round(stockData.loc[currIndex][str(method)], 2)
actualCurrPrice = round(stockData.loc[currIndex]['Close(Act as Actual)'], 2)

diff1 = round(predictCurrPrice - round(stockData.loc[yestIndex][str(method)], 2), 2)
diff2 = round(actualCurrPrice - round(stockData.loc[yestIndex]['Close(Act as Actual)'], 2), 2)


st.header(str(stockName) + " - " +  "Stock Market Prediction")
col1, col2, col3 = st.columns(3)
col1.metric("Date", dateStr, '')
col2.metric("Predicted Price (USD)","$"+ str(predictCurrPrice) , diff1)
col3.metric("Actual Price (USD)", "$"+ str(actualCurrPrice), diff2)

# BELOW FOR THE PLOT

stockDataUpdated = stockData.iloc[currIndex - duration:currIndex]

fig = go.Figure()
fig.add_trace(go.Scatter(x = stockDataUpdated['Date'], y = stockDataUpdated['Close(Act as Actual)' ], line=dict(color='blue'), name = 'Actual Data'))
fig.add_trace(go.Scatter(x = stockDataUpdated['Date'], y = stockDataUpdated[str(method)], line=dict(color='red'), name = str(method)))
st.plotly_chart(fig)