# pip install streamlit fbprophet yfinance plotly
import streamlit as st
from datetime import date
import numpy as np
import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly,plot_components_plotly
from plotly import graph_objs as go
import plotly.express as px
import plotly.figure_factory as ff


st.set_page_config(layout="wide") 

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('Stock Forecast App')

stocks = ('GOOGLE', 'APPLE', 'MICROSOFT')
selected_stock = st.selectbox('Select stock for analysis and prediction', stocks)


st.markdown("""---""")

# get data of selected stock for time period 1-JAN-2015 to Today
@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

stocks_dict = {'GOOGLE' : 'GOOG' , 'APPLE':'AAPL' , 'MICROSOFT':'MSFT'}

data = load_data(stocks_dict[selected_stock])

# Display data in tabular form
st.header('Tabular Data:')

table = go.Figure(data=[go.Table(
   
    header=dict(values=list(['Date' , 'Open' , 'High' , 'Low' , 'Close' ,'Adjusted Close', 'Volume']),
                fill_color='paleturquoise',align='left',font=dict(color='black',size=20),height=30),

    cells=dict(values=[data.Date , data.Open, data.High, data.Low, data.Close ,data['Adj Close'] ,data.Volume],
            fill_color='lavender',height = 30,align='left',font=dict(color='black',size=15)))
])
table.update_layout(width=1800, height=700)

st.write(table)

st.markdown("""---""")

# Display statistics of stocks like all time high, low etc.
st.header('Insights:')
col1,col2,col3 = st.columns(3)

with col1 :
    st.header('All Time High')
    st.title(round(max(data.High),2))

with col2:
    st.header('All Time Low')
    st.title(round(min(data.Low),2))

with col3:
    st.header('52 Week high')
    high_52 = round(max(data.tail(262).High),2)
    st.title(high_52)

with col1:
    st.header('52 Week Low')
    low_52 = round(min(data.tail(262).Low),2)
    st.title(low_52)

with col2:
    st.header('Last Traded Price')
    st.title(round(data.iloc[-1].Close,2))


st.markdown("""---""")


# Display line plot of closing price
st.header(f'Closing price of {selected_stock} over time:')
fig = px.line(data, x=data['Date'], y=data['Close'])
fig.update_layout(width=1800,height=600 )
fig.update_traces(line=dict(color="Light Blue", width=2),)
st.write(fig)


# Slider to selecte number of yeras to forecast
st.header('Select number of years to forecast prices:')
n_years = st.slider(' ', 1, 4)
period = n_years * 365 # convert to no. of days

# Predict forecast with Prophet.
df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Display forecasted data in tabular format
forecast_data = forecast[forecast.ds > df_train.iloc[-1].ds ][['ds' , 'yhat_lower' , 'yhat_upper' , 'yhat']]
forecast_data.rename(columns={'ds':'Date' , 'yhat_lower':'Lower boundary' , 'yhat_upper' : 'Upper boundary' , 'yhat' : 'Predicted price'},inplace=True)

st.header('Forecasted Data:')

forecast_table = go.Figure(data=[go.Table(
   
    header=dict(values=list(forecast_data.columns),fill_color='paleturquoise',align='left',font=dict(color='black',size=20),height=30),
    cells=dict(values=[forecast_data.Date , forecast_data['Lower boundary'] , forecast_data['Upper boundary'] , forecast_data['Predicted price']],
            fill_color='lavender',height = 30,align='left',font=dict(color='black',size=15)))
])
forecast_table.update_layout(width=1800, height=700)

st.write(forecast_table)
st.markdown("""---""")
    
# Line plot of forecasted closing prices.
st.header(f'Forecasted plot for {n_years} years:')
fig1 = plot_plotly(m, forecast)
fig1.update_layout(width = 1800 , height = 900)
st.plotly_chart(fig1)

# Line plots of forecast components
st.header(f'Forecast Components:')
fig2 = plot_components_plotly(m, forecast)
fig2.update_layout(width = 1800 , height = 1800)
fig2.update_traces(line=dict(color="Light Blue"))
st.write(fig2)