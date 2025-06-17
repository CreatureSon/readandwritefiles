import csv
# open the csv file in read mode
sales = open('sales.csv','r')

# using the csv library, create a csv object
# the delimiter ',' tells the program how the columns are seperated
sales_file = csv.reader(sales, delimiter=',')

sale_totals = open('salesreport.csv', 'w+')

sale_totals.write('Customer ID,Total\n')

# skip the first line in the csv file if it contains a header record
next(sales_file)

sales_directory = {}

# using a for loop you can step through the file, one line at a time
for record in sales_file:

    #record[0] = Customer ID
    #record[3] = Subtotal
    #record[4] = Tax Amount
    #record[5] = Freight (Shipping?)
    total = float(record[3]) + float(record[4]) + float(record[5])

    #Update Customer ID with new sale total
    sales_directory[record[0]] = sales_directory.get(record[0], 0) + total

#Saving the dictionary to a csv file of all the Customer Sale Totals    
for customerID, total in sales_directory.items():
    sale_totals.write(f"{customerID},{round(total, 2)}\n")

sale_totals.close()
sales.close()
