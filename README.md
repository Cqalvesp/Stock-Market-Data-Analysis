# **Data Pipeline for Stock Market Data Analysis**

This project is a data pipeline that **extracts**, **transforms**, and **loads** (ETL) stock market data from `yfinance`, processes it, stores it in a **MySQL database**, and allows for analysis using **R**. The pipeline is designed to facilitate automated data collection and preprocessing, followed by comprehensive analysis in **R Markdown**.

## **Project Overview**
This pipeline pulls stock market data from `yfinance`, processes and transforms the data, then stores it in a **MySQL** database. The data includes historical stock prices, financial metrics, and stock actions (like dividends, splits). After the data is loaded into the database, the analysis is performed in **R** using **R Markdown**, which produces insights such as statistical summaries, trends, and visualizations.

## **Technologies Used**
- **Python**  
  - `pandas` – for data extraction, transformation, and preprocessing
  - `numpy` – for numerical operations
  - `pymysql` and `sqlalchemy` – for connecting to MySQL database
- **R**  
  - **R Markdown** – for performing and documenting analysis
- **MySQL** – for storing the data
- **yfinance** – extracting stock market data from yahoo finance

## **Data Sources**
- Data is pulled from **Yahoo Finance** using the `yfinance` Python library. The pipeline extracts financial data such as stock prices, historical data, and corporate actions like dividends and splits.

## **Database Structure**
The data is loaded into a **MySQL** database, which includes the following tables:
- **Historical Data**: Stores stock price data over time.
- **Financials**: Stores financial metrics such as earnings, revenue, etc.
- **Stock Actions**: Stores stock actions like dividends and splits.

### **Table Schema (example)**
- **Historical Data**: `date`, `symbol`, `open`, `close`, `high`, `low`, `volume`
- **Financials**: `symbol`, `date`, `earnings`, `revenue`, `profit_margin`, etc.
- **Stock Actions**: `symbol`, `date`, `action_type`, `amount`

## **How the Pipeline Works**
1. **Extract**: Data is pulled from `yfinance` using the stock symbols of interest.
2. **Transform**: The extracted data is cleaned and preprocessed using **pandas** and **numpy** to handle missing values, correct data types, and format the data.
3. **Load**: The processed data is loaded into the **MySQL** database using `pymysql`, with separate tables for historical data, financials, and stock actions.
4. **Analysis**: The transformed data is analyzed using **R** and documented using **R Markdown**. The analysis includes statistical insights, visualizations, and other relevant metrics.
5. **View**: Download html file to see how the data is analyzed.

## **Next Steps**
1. Build AI model to analyze historical data and company financials to predict stock price
2. Docker for containerization
3. AWS for database hosting and model deployment

file:///Users/chrisap/Documents/GitHub/Financial-Data-Pipeline/ML_And_Plots.html

