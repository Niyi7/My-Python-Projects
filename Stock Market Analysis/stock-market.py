import pandas as pd
import yfinance as yf
from datetime import date, timedelta
import plotly.graph_objects as go
import plotly.express as px

today = date.today()

d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=365)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2

data = yf.download('GOOG', start=start_date, end=end_date, progress=False)
data["Date"] = data.index
data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
data.reset_index(drop=True, inplace=True)
print(data.head())

# Candlestick Visualization
figure = go.Figure(data=[go.Candlestick(x=data["Date"], open=data["Open"], high=data["High"], low=data["Low"], close=data["Close"])])
figure.update_layout(title = "Google Stock Price Analysis", xaxis_rangeslider_visible=False)
figure.show()

# Bar Chart Visualization
figure = px.bar(data, x = "Date", y= "Close")
figure.show()

# line Chart with Range Slider - for x-axis
figure = px.line(data, x='Date', y='Close', title='Stock Market Analysis with Rangeslider')
figure.update_xaxes(rangeslider_visible=True)
figure.show()

# for y-axis
figure = px.line(data, x='Date', y='Close', title="Y-Axis Range Slider for Stock Market Analysis")
figure.update_yaxes(rangemode='tozero')  # Use 'tozero' for the range slider
figure.show()

figure = px.line(data, x='Date', y='Close', title='Stock Market Analysis with Time Period Selectors')

# time period selectors
figure = px.line(data, x='Date', y='Close', title='Stock Market Analysis with Rangeslider')
figure.update_xaxes(
    rangeselector=dict(
        buttons=list([dict(count=1, label="1m", step="month", stepmode="backward"),dict(count=3, label="3m", step="month", stepmode="backward"), dict(count=6, label="6m", step="month", stepmode="backward") , dict(count=1, label="1y", step="year", stepmode="backward"), dict(step="all")
        ])
    )
)
figure.show()

# Remove weekends - Sat and Sun
figure = px.scatter(data, x='Date', y='Close', range_x=['2022-11-08', '2023-11-07'],
                 title="Stock Market Analysis by Hiding Weekend Gaps")
figure.update_xaxes(
    rangebreaks=[
        dict(bounds=["sat", "sun"])
    ]
)
figure.show()