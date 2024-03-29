# INF601 - Advanved Programming in Python
# Janelyn Nichols
# Mini Project 1

import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import copy
import os
import pathlib as Path


#(5/5 points) Initial comments with your name, class and project at the top of your .py file.
#(5/5 points) Proper import of packages used.
#(20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your favorite stock tickers for the last 10 trading days.
#(10/10 points) Store this information in a list that you will convert to a array in NumPy.
#(10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring the documentation for matplotlib. At minimum it just needs to show 10 data points.
#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#(10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.

tickers = ["MSFT", "TSLA", "SONY", "META", "ANET"]

try:
    os.mkdir("C:\charts")
except FileExistsError:
    pass

for ticker in tickers:
    myticker = yf.Ticker(ticker)
    history = myticker.history(period="10d")

    closingList = []

    for price in history['Close']:
        closingList.append(price)

    print(closingList)

    lowprice = copy.copy(closingList)
    lowprice.sort()
    low_price = lowprice[0]
    high_price = lowprice[-1]

    myarray = np.array(closingList)
    plt.plot(myarray)
    plt.xlabel("Days")
    plt.ylabel("Closing Price")
    plt.title(f"{ticker} Closing Price")
    plt.axis((1, 10, low_price-2, high_price+2))
    plt.show()

    filename = "charts/" + ticker + ".png"
    plt.savefig(filename)
    plt.show()








