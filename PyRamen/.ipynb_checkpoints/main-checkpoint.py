# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('./menu_data.csv')
sales_filepath = Path('./sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data

menu = []
sales = []

# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Read in the menu data into the menu list

with open(menu_filepath, 'r') as menufile:
    
    menureader = csv.reader(menufile, delimiter=',')
    
    header = next(menureader)
    
# @TODO: Read in the sales data into the sales list

with open(sales_filepath, 'r') as salesfile:
    
    salesreader = csv.reader(salesfile, delimiter=',')
    
    header = next(salesreader)

# @TODO: Loop over every row in the sales list object

    for row in salesreader:
        int(row[0])
    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
        sales.append(row)
print(sales)