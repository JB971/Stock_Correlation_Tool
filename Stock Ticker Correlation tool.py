# using yfinance and pandas to pull and manipulate data

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# this allows the user to input any two stocks 

st1_input = input('Input the 1st stock ticker: ')
st1_input = st1_input.upper()
st2_input = input('Input the 2nd stock ticker: ')
st2_input = st2_input.upper()

# this takes the inputs and retrieves the data from yfinance

stock1 = yf.Ticker(st1_input)
stock2 = yf.Ticker(st2_input)

# these lines separate out Close prices for comparison

stock1_h = stock1.history(period='1y')
stock1_df = pd.DataFrame(stock1_h)
stock1_close = pd.DataFrame(stock1_df['Close'])
stock1_change = stock1_close.pct_change(1)

stock2_h = stock2.history(period='1y')
stock2_df = pd.DataFrame(stock2_h)
stock2_close = pd.DataFrame(stock2_df['Close'])
stock2_change = stock2_close.pct_change(1)

# corrwith is used to get the actual correlation number

stocks = stock1_change.corrwith(stock2_change, axis=0, method='pearson')

print('The 1 Year correllation of the closing price between', st1_input, 'and', st2_input, 'is:', stocks.to_string(index=False))

# Now the cumulative sum is calculated and plotted to a line graph

plt.plot(stock1_change.cumsum(), label=st1_input)
plt.plot(stock2_change.cumsum(), label=st2_input)
plt.ylabel('Percentage Change')
plt.legend()
plt.show()





