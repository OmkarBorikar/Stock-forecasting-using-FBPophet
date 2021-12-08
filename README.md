# Stock-forecasting-using-FBPophet

* **Brief Overview of project**

Goal of this project is to analyse and get insights of stock and forecast price of stock for selected number of years.

Name of stock to be analysed can be any from following list - Google , Microsoft and Apple.

Data for selected stock is collected from yfinance API. Data from 1st Januray 2015 to todays' date is considered for analysis and forecast.

Facebbook Prophet library is used for forecasting data of selected stock for selected period of time.

Streamlit framework is used for building web application.

* **Overview of web app components**

This web app can be accessed from here - [Stock Forecasting Using FbProphet](https://share.streamlit.io/omkarborikar/stock-forecasting-using-fbpophet/main/app.py)

After opening the web app following page will be opened.

Any of 3 (Google, Microsoft and Apple) stock can be selected for analysis and forecast.
After selecting stock tabular data of stock is displayed. This data is dated from 1st Januray 2015 to todays' date.

![image](https://user-images.githubusercontent.com/82905366/145240665-2208b831-1927-4825-85f1-9b3dc3c29eec.png)

Next section displays insights of stock such

      All time high
      All time low
      52 week high
      52 week low
      LTP (Last traded price)
      
Following this, line plot is displayed of closing price from 2015 to todays' date.

![image](https://user-images.githubusercontent.com/82905366/145245170-c152b042-eddd-458e-ac2e-5b3f5f3c8f7b.png)

Number of years for which stock price needs to be forecasted can be selected using slider. After selecting number of years , predicted data is displayed in tabular format. Table contains following columns - 
    
      Date : Date for which prediction is made
      Lower boundary : Lower boundary of prediction.
      Upper boundary : Upper boundary of prediction
      Predicted price : Actual predicted price
      
![image](https://user-images.githubusercontent.com/82905366/145255017-e0419b4b-f43b-4cff-b0fb-57903b402924.png)

Line plot for predicted price is displayed. Black coloured points in plot represent actual price and blue line represents predicted price.

![image](https://user-images.githubusercontent.com/82905366/145255404-86c763ed-e0e5-446e-b099-86e18e3927a1.png)

Lastly forecasted components are displayed such as - trend (decreasing or increasing) , yearly trend and weekly trend.

![image](https://user-images.githubusercontent.com/82905366/145255739-b3fcd4e5-40f7-4202-bb05-35793c360a57.png)






