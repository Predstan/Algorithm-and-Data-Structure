# Applying MultiArray to print Store Data

from MultiArray import MultiArray
from Array import Array
import datetime


# Returs a 3-D array of the data from a txt file
def extract(filename):

    # Opens File
    filename = open(filename, "r")

    # Reads first two line of txt file 
    num_of_stores = int(filename.readline()) # First line contains number of Store
    num_of_items = int(filename.readline()) # Second line contains Number of items in each store

    months = 12 # January to December Month for sales record

    # Creates the 3-D Array using the Dimensions "store, item number and the months"
    salesData = MultiArray(num_of_stores, num_of_items, months)

    # Iterates over the remaining lines for Valuee recorded
    # According to the Format, each lines has four elements
    # first is the Store number
    # Second is the Months
    # Third is the item number
    # Fourth is the sales recorded
    for lines in filename:
        lines = lines.strip()
        storendx = int(lines[0]) - 1
        itemsndx = int(lines[2]) - 1
        monthsndx = int(lines[1]) - 1
        sales = float(lines[3])
        salesData[storendx, itemsndx, monthsndx]= sales
    
    return salesData

# Retruns the total sales for a store
def total_sales_by_store(salesData, store):
    
    # the store index is offset
    store = store - 1
    total = 0.0

    # Iterate over the Item number
    for item in range(salesData.length(2)):

        # Iterate over the months
        for month in range(salesData.length(3)):

            # Gets the item at the index, s, i, m
            total += salesData[store, item, month]

    return total

# Returns the total sales by month in every store
def total_sales_by_month(salesData, month):
    
    # the month index is offset
    month = month - 1

    total = 0.0

    # Iterate over the Store number
    for store in range(salesData.length(1)):

        # Iterate over the item number
        for item in range(salesData.length(2)):

            total+= salesData[store, item, month]
        
    return total

# Returns the total sales by item number
def total_sales_by_item(salesData, item):

    # Offset of the item number
    item = item - 1

    total = 0.0

    # Iterate over the Store number
    for store in range(salesData.length(1)):

        # Iterate over the Months index
        for month in range(salesData.length(3)):

            total += salesData[store, item, month]

    return total

# Returns the total sales per Month for a Store
def total_sales_per_month(salesData, store):

    # Offset of the store number
    store = store - 1

    # Creates an Array to store the total sales of each month
    total = Array(12)
    
    # Iterate over the Months
    for month in range(salesData.length(3)):
        sum = 0.0
        # Iterate over the item number
        for item in range(salesData.length(2)):

            sum += salesData[store, item, month]

        total[month] = sum

    return total

# Displays the Report of a particular store
def Display_store_report(salesData, store):

    print("LazyMart Sales Report".center(90))
    print("\n")
    print( "Store "+ "#" + str(store)).center(90)
    months = []  # 
    months.append("Item #")

    for i in range(12):
        month_number = str(i+1)
        datetime_object = datetime.datetime.strptime(month_number, "%m")
        month_name = datetime_object.strftime("%b")
        months.append(month_name)

    print("    ".join(months))

    store = store - 1
    
    for item in range(salesData.length(2)):
        sales_monthly = []
        sales_monthly.append(item+1)
        for month in range(salesData.length(3)): 
            sales_monthly.append(salesData[store, item, month])

        print("    ".join(sales_monthly))

# Returns total sales for each store sorted by total sales from largest to smallest
def Total_sales(salesData):

    sales = {}

    for store in range(salesData.length(1)):
        total = 0.0

        for item in range(salesData.length(2)):

            for month in range(salesData.length(3)):
                total += salesData[store, item, month]
        store = "store"+str(store)
        sales[store] = total


    sales = sorted(sales.items(), key=lambda x: x[1], reverse= True)

    return sales

# Returns total sales for each item sorted by item number
def total_item_sales(salesData):

    # Creates a 1-D Array to store the total sales
    sales = Array(100)

    # Iterate over the item number
    for item in range(salesData.length(2)):
        total = 0

        # Iterate over the store number
        for store in range(salesData.length(1)):

            # Iterate over the months
            for month in range(salesData.length(3)):

                # Sums the sales numeber
                total += salesData[store, item, month]
        # Sets the item into the Array        
        sales[item] = total

    return sales


