# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('Resources/menu_data.csv')
sales_filepath = Path('Resources/sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []
report =  {}

# @TODO: Read in the menu data into the menu list
with open(menu_filepath, 'r') as csvfile:
   # print(csvfile)
    
    csv_reader = csv.reader(csvfile, delimiter = ',')
    header = next(csv_reader)
    
    # print(f"{header} 
    
    for row in csv_reader:
        menu.append(row)
        
        # menu_data[row[0]] = row[1], row[2], row[3], row[4]]




# @TODO: Read in the sales data into the sales list
with open(sales_filepath, 'r') as csvfile:
    # print(csvfile)
    
    csv_reader = csv.reader(csvfile, delimiter = ',')
    header = next(csv_reader)
    
    # print(f"{header}
    
    for roe in csv_reader:
        sales.append(row)
        
        # sales_data[row[0], row[1], row[2], row[3], row[4]]


# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object
for sale in sales_data:
quantity = int(sale[3])
sales_item = sale [4]




    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    
    


    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    if report.get(sales_item) == None:
        report[sales_item] = {"01-count": 0,
                              "02-revenue": 0,
                              "03-cogs" : 0,
                              "04-profit" : 0}








    # @TODO: For every row in our sales data, loop over the menu records to determine a match


        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables




        # @TODO: Calculate profit of each item in the menu data
        menu = menu_data[sales_item]


        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        
        if menu! = None:
            price = float(menu[2])
            cost = float(menu[3])
            profit = quantity * (price - cost)
            report[sales_item]["01-count"] += quantity
            report[sales_item]["02-revenue"] += price * quantity                 
            report[sales_item]["03-cogs"] += cost * quantity
            report[sales_item]["04-profit"] += profit * quantity
        else:
            print(f"{sales_item} does not contain data')

            # @TODO: Print out matching menu data

            for sales_item in report:
                print(f'{sales_item} : {report[sales_item]}')




            # @TODO: Cumulatively add up the metrics for each item key





        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match



    # @TODO: Increment the row counter by 1


# @TODO: Print total number of records in sales data




# @TODO: Write out report to a text file (won't appear on the command line output)
        for sales_item in report:
            print(f'{sales_item} : {report[sales_item]}')
