import csv
# open the csv file in read mode
customers = open('customers.csv','r')

# using the csv library, create a csv object
# the delimiter ',' tells the program how the columns are seperated
customer_file = csv.reader(customers, delimiter=',')

customer_countries = open('customer_country.csv', 'w+')

customer_countries.write('Full Name,Country\n')

# skip the first line in the csv file if it contains a header record
# in this file it would be "ID,FirstName,LastName,City,Country,Phone"
next(customer_file)

# using a for loop you can step through the file, one line at a time
for record in customer_file:
    
    #record[1] = First Name
    #record[2] = Last Name
    #record[4] = Country
    customer_countries.write(record[1] + ' ' + record[2] + "," + record[4] + "\n")

customer_countries.close()
customers.close()
