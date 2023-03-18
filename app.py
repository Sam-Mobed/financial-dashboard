from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates", static_folder="static")

#how index.html is going to be organized. 
#dark mode and white mode for the page
#one header file that follows you as you scroll. (with link to my github and linkedin)
#title
#simple about paragraph, why and how to use the dashboard
#in the og main.py, you can only compare two stocks. in the new version, you start with one, and can compare up to 6 plots.
#you have a list of stocks that you're investing in. the date when you initially put the sum, and the amount. it will calculate your current holding and display
#the rest of the graphs. 
#besides the candlestick graphs, you will have a pie chart showing the diversification of your portfolio
#technical stock analysis, will make a an RSI plot, super long x axis you can scroll of a specific stock to show the progression overtime
#and a prediction for stock prices, you select a stock and it will generate a graph for you
#a stock screener
#and maybe a backtesting stock trading strategy plots, maybe

#there is only an index.html file, no other pages
#when the page starts running,
"""
There is only an index.html file, no other pages on the website.
When the page starts running, graphs of some sample stock are generated on the page, just so it's not empty.
Every time a user enters parameters for some specific graph, that graph is updated according to the new parameters.

"""

"""
@app.route('/', methods="POST")
def mystocks():
    pass #one for the list of the stocks with add/remove methods. besides each stock is the current price+if it went up or down
    you can do this using a stock screener tutorial
    
def stocksTable():
    a table of the stocks that the user has actually invested in. the initial sum + the date when he put the money in.
    and inside the table you can see the  current profit/loss. a graph can probably be made out of this. we'll see (analyzing stock price correlations maybe?)
    graph: x-axis: time, intiial investment date, current date, and the fluctuation of that investment is the plot, y-axis is the price of that stock

def generatePieChart():
    this function will generate a pie chart showing the diversification of portfolio based on the stocks inside StocksTable. 
    based on how many slices or wtv, a small text is generated making recommendations (invest in more, do this or that, nothing crazy)

@app.route('/', methods="POST")
def generatePrediction():
    pass
    
def generateStrategy:
    backtesting stock trading strategy. 
    this one is going to generate a new html file, it's fine. it can be shown as a new tab not a big deal. 

        
"""
@app.route('/', methods="POST")
def generateCandleStick():
    pass



@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
