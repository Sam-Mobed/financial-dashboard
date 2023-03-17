#core python packages
import math
import datetime as dt
#external packages
import numpy as np
import yfinance as yf

from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.layouts import row, column
from bokeh.models import TextInput, Button, DatePicker, MultiChoice
"""
achieved through these external python packages
bokeh for interactive web visualization
numPy for array handling
yfinance to extract stock data from the Yahoo finance API
"""

#load the data from the API
def load_data(ticker1, ticker2, start, end):
    df1 = yf.download(ticker1, start, end)
    df2 = yf.download(ticker2, start, end)
    return df1, df2

#Plot the loaded data
def plot_data(data, indicators, sync_axis=None):
    #we want to plot a candlestick chart with optional indicators
    df = data
    #there will be days with gains, and days with losses
    gain = df.Close > df.Open
    loss =  df.Open > df.Close
    width_candlestick = 12 * 60 * 60 * 1000

    if sync_axis is not None:
        plot = figure(x_axis_type="datetime", tools="pan,wheel_zoom,box_zoom,reset,save", width=1000, x_range=sync_axis)
    else:
        plot = figure(x_axis_type="datetime", tools="pan,wheel_zoom,box_zoom,reset,save", width=1000)
    
    plot.xaxis.major_label_orientation = math.pi/4
    plot.grid.grid_line_alpha = 0.25

    #here we specify the starting point and the end point
    plot.segment(df.index, df.High, df.index, df.Low, color="black")
    #plot the actual candlestick,vertical for every gain and every loss
    plot.vbar(df.index[gain], width_candlestick, df.Open[gain], df.Close[gain], fill_color= "#00ff00", line_color= "#00ff00")
    plot.vbar(df.index[loss], width_candlestick, df.Open[loss], df.Close[loss], fill_color= "#ff0000", line_color= "#ff0000")

    for indicator in indicators:
        if indicator == "30 Day SMA":
            df['SMA30'] = df['Close'].rolling(30).mean()
            plot.line(df.index, df.SMA30, color="purple", legend_label="30 Day SMA")
        elif indicator == "100 Day SMA":
            df['SMA100'] = df['Close'].rolling(100).mean()
            plot.line(df.index, df.SMA100, color="blue", legend_label="100 Day SMA")
        elif indicator == "Linear Regression Line":
            par = np.polyfit(range(len(df.index.values)), df.Close.values, 1, full=True)
            slope = par[0][0]
            intercept = par[0][1]
            y_pred = [slope * i + intercept for i in range (len(df.index.values))]
            plot.segment(df.index[0], y_pred[0], df.index[-1], y_pred[-1], legend_label="Linear Regression", color="Red")

        plot.legend.location = "top_left"
        plot.legend.click_policy = "hide"


    return plot

#handle button clicks
def on_button_click(ticker1, ticker2, start, end, indicators):
    df1, df2 = load_data(ticker1,ticker2,start,end)
    plot1 = plot_data(df1, indicators)
    plot2 = plot_data(df2, indicators, sync_axis=plot1.x_range)
    curdoc.clear()
    curdoc().add_root(layout)
    curdoc().add_root(row(plot1,plot2))

#Interface
stock1_text = TextInput(title="Stock 1")
stock2_text = TextInput(title="Stock 2")
date_picker_start = DatePicker(title="Start Date", value="2020-01-01",
 min_date="2000-01-01", max_date=dt.datetime.now().strftime("%Y-%m-%d"))

date_picker_end = DatePicker(title="End Date", value="2020-02-01",
 min_date="2000-01-01", max_date=dt.datetime.now().strftime("%Y-%m-%d"))

#indicator choice 
"""
instead of just plotting the stock price, we also want to plot some indicators
although further down the line, more technical analysis stuff will be added
for now, we are only going to do the 30-day moving avg, the 100-day moving avg
alongside a linear regression line
"""
indicator_choice = MultiChoice(options=["100 Day SMA", "30 Day SMA", "Linear Regression Line"])

#interactive button
load_button = Button(label="Load Data", button_type="success")
load_button.on_click(lambda: on_button_click(stock1_text.value, stock2_text.value, date_picker_start.value,date_picker_end.value,indicator_choice.value))

#create a column layout, the arguments will be stacked on top of eachother
layout = column(stock1_text, stock2_text, date_picker_start, date_picker_end, indicator_choice, load_button)

curdoc().clear()
curdoc().add_root(layout)

#if __name__==__main__