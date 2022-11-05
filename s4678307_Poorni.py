import csv                                       # imported the csv module.

# 1. Calculating the average salary of employee type: Manager.

file = open("employees.csv", "r")                # opened the given csv file to read.

try:                                             # used try statement for further processing.
    csv_reader = csv.reader(file)                # used csv_reader to read the contents of csv file.
    total = 0                                    # created variable to calculate total.
    i = 0                                        # created variable to iterate.
    for column in csv_reader:                    # used for loop to iterate columns in csv file.
        if column[3] == "Manager":               # used if statement to choose employee type: Manager.
            total = total + int(column[2])       # added total entries of column[2] with employee type: Manager.
            i = i + 1                            # iterated the entries of column[2] with employee type: Manager.
    print("The average salary is $", int(total / i), ".")
    # printing average salary by dividing total salary amount of managers from the number of manager employees.
    # used int to match the given output.

finally:                                         # used finally statement to close file.
    file.close()


# 2. Finding the staff member with the lowest salary.

file = open("employees.csv", "r")                # opened the given csv file to read.

try:                                             # used try statement for further processing.
    csv_reader = csv.reader(file)                # used csv_reader to read the contents of csv file.
    row = 0                                      # created variable for lower bound.
    lowest_value = int(column[2]) + 1            # created variable to find the lowest value.
    for column in csv_reader:                    # used for loops to iterate columns in csv file.
        if row > 0 and int(column[2]) <= lowest_value:  # using if statement to choose column[2].
            lowest_value = int(column[2])        # used lowest value to find the lowest salary in column[2].
            name = column[0] + " " + column[1]   # added column to get full name.
        row = row + 1                                 # iterated rows to find the lowest salary.
    print(name, " has the lowest salary ( $",float(lowest_value),").")
    # printing the full name of the staff member with the amount who has the lowest salary.
    # using float to match the given output.

finally:                                         # used finally statement to close file.
    file.close()

