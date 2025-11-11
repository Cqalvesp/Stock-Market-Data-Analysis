# Module to run all scripts at once to update database, web server, and Visualizations
import data_prep.data_cleaning as cleaning
import data_prep.data_collection as collection

# Run functions and print statements
if __name__ == "__main__":
    # Truncate all tables in database
    collection.Truncate()
    print("Database tables have been truncated.")
    
    # Run cleaner module functions on fetched data and insert to database
    for i in range(len(collection.Stock_List)):
        ticker = collection.Stock_List[i]
        name = collection.Company_Names[i]

        # Data transfer function to send company names and tickers to database
        collection.Name_Insert(ticker, name) 
        print("Company names and tickers have been inserted to database.") 

        # Fetch data, clean it, and send it to the database
        hist = collection.stock_history(ticker)
        hist = cleaning.clean_hist(hist)
        collection.History_Insert(ticker, hist)
        print("Company history has been inserted to database.") 
    
        act = collection.stock_actions(ticker)
        act = cleaning.clean_acts(act)
        collection.Actions_Insert(ticker, act)
        print("Company actions have been inserted to database.") 

        fin = collection.stock_financials(ticker)
        fin = cleaning.clean_fins(fin)
        collection.Financial_Insert(ticker, fin)
        print("Company financials have been inserted to database.") 
