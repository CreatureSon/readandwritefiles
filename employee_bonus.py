import csv
# open the csv file in read mode
bonuses = open('employee_data.csv','r')

# using the csv library, create a csv object
# the delimiter ',' tells the program how the columns are seperated
bonuses_file = csv.reader(bonuses, delimiter=',')

# skip the first line in the csv file if it contains a header record
next(bonuses_file)

# using a for loop you can step through the file, one line at a time
for record in bonuses_file:

    #record[1] = Name
    #record[3] = Salary
    #record[7] = Bonus
    print('Name:',record[1])
    print(f'Salary: $ {int(record[3]):>10,.2f}')
    print(f'Bonus:  $ {(int(record[3]) * float(record[7])):>10,.2f}')
    print(f'Pay:    $ {(int(record[3]) + (int(record[3]) * float(record[7]))):>10,.2f}')

    # this command will pause the program until a key is pressed
    input()