# Receives data from each part of a stock ticker class
# Converts data into separate data frames 
# Removes columns and rows from data frames deemed unnecessary

# Necessary library imports
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Function to preprocess and transform historical data
def clean_hist(history):
    # Changes to Date Column
    history = history.reset_index()
    history['Date'] = pd.to_datetime(history['Date'])
    history['Date'] = history['Date'].dt.date
    
    # Remove 'Dividends' and 'Stock Splits' columns because they are in actions
    history = history.drop(columns=['Dividends'])
    history = history.drop(columns=['Stock Splits'])
    history = history.drop(columns=['index'])

    return history

def clean_acts(actions):
    # Changes to Date Column
    actions = actions.reset_index()
    actions['Date'] = pd.to_datetime(actions['Date'])
    actions['Date'] = actions['Date'].dt.date

    # Track action data up to 1 year ago
    one_year_ago = datetime.now() - timedelta(days=365)
    actions = actions[actions['Date'] >= one_year_ago.date()]

    return actions

def clean_fins(financials):
    # Altering financials dataframe
    financials = financials.rename(columns={"index": "Date"})
    financials['Date'] = financials['Date'].dt.date

    # List of prefixes for columns to drop
    cols_to_keep = ['Date', 'Net Interest Income', 'Interest Expense', 'Interest Income', 'Normalized Income', 'Total Expenses', 'Total Operating Income As Reported',
                    'Net Income Common Stockholders', 'Net Income', 'Tax Provision', 'Pretax Income', 'Operating Income', 'Operating Expense', 'Research And Development',
                    'Gross Profit', 'Cost Of Revenue', 'Total Revenue', 'Operating Revenue']
    
    # Remove columns from the data frame that won't be used in analysis
    for col in financials.columns:
        if col not in cols_to_keep:
            del financials[col]

    return financials
