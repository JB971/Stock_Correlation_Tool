# Stock_Correlation_Tool
A simple tool to show the correlation in the movement of two different stocks or other instruments (futures, crypto, etc.)


What it does:
* The Stock Correlation Tool provides the user with the statistical correlation between two stocks or other trading instruments.  It also shows a simple visualization in the form of a line graph.


Intended Use:
* It is intended to add context to the relationship of two trading instruments so the trader can make a more informed decision when trading.


How it works:
* The tool is based on Python code and uses the yfinance, pandas, and matplotlib libraries.  
* Currently, it only works within the Python console.
* When run the tool will prompt the user to enter the tickers of two stocks or other trading instruments(using the nomenclature on Yahoo Finance).
* After the two trading instruments are entered, the tool will retrieve the relevant historical data from yfinance and process it through pandas as a dataframe.  It will then print the statement containing the correlation number (shown in a range from -1 to 1).
* The tool will also display a simple line graph of the historical percentage change over time of the two trading instruments.


Future Goals:
* Allow the user to change the time frame of the correlation study.  Currently, it is set at 1 year.
* Create a graphical interface, so the tool can be used outside of the Python console.
