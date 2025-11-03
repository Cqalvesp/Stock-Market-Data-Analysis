# Data framing libraries
import pandas as pd
import numpy as np
import yfinance as yf

# Custom Modules
import data_cleaning as cl
from db_connection import get_connection

# Define stock tickers to track and create ticker object for each
Stock_List = ["AAPL", "MSFT", "NVDA", "AVGO", "ORCL", "CRM", "CSCO", "IBM", "ACN", "ADBE"]
Company_Names = ["Apple Inc", "Microsoft Corp", "Nvidia Corp", "Broadcom Inc", "Oracle Corp", 
                 "Salesforce Inc", "Cisco Systems Inc", "IBM Common Stock", "Accenture Plc", "Adobe Inc"]
Stock_Tickers = {x : yf.Ticker(x) for x in Stock_List}


# Use stockClass to pull each attribute from given stock
def stock_history(stock):
    item = Stock_Tickers[stock]
    return item.history(period="1y", interval="1d").reset_index()

def stock_actions(stock):
    item = Stock_Tickers[stock]
    return item.actions.reset_index()

def stock_financials(stock):
    item = Stock_Tickers[stock]
    return item.financials.T.reset_index()

def Truncate():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # Delete all data from tables in database
            cursor.execute("DELETE FROM history;")
            cursor.execute("DELETE FROM actions;")
            cursor.execute("DELETE FROM financials;")
            cursor.execute("DELETE FROM companies;")

    finally:
        conn.commit()
        conn.close()
    return None

# Check if the column is part of the dataframe being inserted
def column_check(row, column):
    if column in row:
        return row[column]
    else: 
        return None

# Function to move cleaned data to database
def Name_Insert(Ticker, Name):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            query = "INSERT INTO companies (StockTicker, CompanyName) VALUES (%s, %s)"
            cursor.execute(query, (Ticker, Name))

    finally:
        conn.commit()
        conn.close()
    return None

# Insert history data frame to MySQL database
def History_Insert(Ticker, History_df):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            for index, row in History_df.iterrows():
                query = "INSERT INTO history (StockTicker, Open, High, Low, Close, Volume, Date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (Ticker, row['Open'], row['High'], row['Low'], row['Close'], row['Volume'], row['Date']))

    finally:
        conn.commit()
        conn.close()
    return None

# Insert action data frame to MySQL database
def Actions_Insert(Ticker, Actions_df):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            for index, row in Actions_df.iterrows():
                query = "INSERT INTO actions (StockTicker, Date, Dividends, Splits) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (Ticker, row['Date'], row['Dividends'], row['Stock Splits']))

    finally:
        conn.commit()
        conn.close()
    return None

# Insert financials data frame to MySQL database
def Financial_Insert(Ticker, Financials_df):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            for index, row in Financials_df.iterrows():
                row = row.where(pd.notnull(row), None)

                query = "INSERT INTO financials (StockTicker, Date, NetInterestIncome, InterestExpense, InterestIncome, " \
                "NormalizedIncome, TotalExpenses, ReportedOperatingIncome, StockholderNetIncome, NetIncome, TaxProvision, " \
                "PretaxIncome, OperatingIncome, OperatingExpense, ResearchAndDevelopment, GrossProfit, CostOfRevenue, TotalRevenue, OperatingRevenue) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

                cursor.execute(query, (Ticker, 
                                       row['Date'], 
                                       column_check(row, 'Net Interest Income'), 
                                       column_check(row, 'Interest Expense'), 
                                       column_check(row, 'Interest Income'), 
                                       column_check(row, 'Normalized Income'), 
                                       column_check(row, 'Total Expenses'),
                                       column_check(row, 'Total Operating Income As Reported'), 
                                       column_check(row, 'Net Income Common Stockholders'), 
                                       column_check(row, 'Net Income'), 
                                       column_check(row, 'Tax Provision'), 
                                       column_check(row, 'Pretax Income'),
                                       column_check(row, 'Operating Income'), 
                                       column_check(row, 'Operating Expense'), 
                                       column_check(row, 'Research And Development'), 
                                       column_check(row, 'Gross Profit'), 
                                       column_check(row, 'Cost Of Revenue'), 
                                       column_check(row, 'Total Revenue'),
                                       column_check(row, 'Operating Revenue')))

    finally:
        conn.commit()
        conn.close()
    return None

   

# Run functions and print statements
if __name__ == "__main__":
    # Truncate all tables in database
    Truncate()
    print("Database tables have been truncated.")
    
    # Run cleaner module functions on fetched data and insert to database
    for i in range(len(Stock_List)):
        ticker = Stock_List[i]
        name = Company_Names[i]

        # Data transfer function to send company names and tickers to database
        Name_Insert(ticker, name) 
        print("Company names and tickers have been inserted to database.") 

        # Fetch data, clean it, and send it to the database
        hist = stock_history(ticker)
        hist = cl.clean_hist(hist)
        History_Insert(ticker, hist)
        print("Company history has been inserted to database.") 
    
        act = stock_actions(ticker)
        act = cl.clean_acts(act)
        Actions_Insert(ticker, act)
        print("Company actions have been inserted to database.") 

        fin = stock_financials(ticker)
        fin = cl.clean_fins(fin)
        Financial_Insert(ticker, fin)
        print("Company financials have been inserted to database.") 

    
        
        
        
    