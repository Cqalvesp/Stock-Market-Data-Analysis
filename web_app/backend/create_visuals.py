# Visualization Libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Data Manipulation Libraries
import pandas as pd
import numpy as np

# Database Connection Module
from data_prep.db_connection import get_connection

actions_query = "SELECT * FROM actions;"
financials_query = "SELECT * FROM financials;"
history_query = "SELECT * FROM history;"

actions = pd.read_sql('file_path')
financials = pd.read_sql('file_path')
history = pd.read_sql('file_path')

def create_line_chart():
    pass

def create_scatter_plot():
    pass

def create_cluster():
    pass