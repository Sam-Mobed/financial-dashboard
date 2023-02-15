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
    df1 = yf.downloard(ticker1, start, end)
    df2 = yf.download(ticker2, start, end)
    return df1, df2

#Plot the loaded data
def plot_data(data, indicators, sync_axis=None):
    pass

#handle button clicks
def on_button_click(ticker1, ticker2, start, end, indicators):
    pass

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
layout = column(stock1_text, stock1_text, date_picker_start, date_picker_end, indicator_choice, load_button)

#build an interactive UI around the Plots






#if __name__==__main__