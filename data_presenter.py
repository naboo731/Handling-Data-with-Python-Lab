
import matplotlib.pyplot as graph
cupcake_invoices = open("CupcakeInvoices.csv")

# Loop through all the data and print each row.
for line in cupcake_invoices:
    print(line)

# Loop through all the data and print the type of cupcakes purchased.
cupcake_invoices.seek(0, 0)
for line in cupcake_invoices:
    if 'Chocolate' in line:
        print('Chocolate')
    elif 'Vanilla' in line:
        print('Vanilla')
    elif 'Strawberry' in line:
        print('Strawberry')

# Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).
cupcake_invoices.seek(0, 0)
for line in cupcake_invoices:
    for line in cupcake_invoices:
        total = 0
        value = line.split(',')
        total = total + (float(value[-1]) * float(value[-2]))
        print(total)

# Loop through all the data, and print out the total for all invoices combined.
cupcake_invoices.seek(0, 0)

for line in cupcake_invoices:
    total = 0
    value = line.split(',')
    total = total + (float(value[-1]) * float(value[-2]))
print(total)

cupcake_invoices.close()


# Advanced

# x axis values
x = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
# corresponding y axis values
y = [20, 30, 42, 64, 60, 52, 21]

# plotting the points
graph.plot(x, y)

# naming the x axis
graph.xlabel('Day Purchased')
# naming the y axis
graph.ylabel('Cupcakes Purchased')

# giving a title to my graph
graph.title('My Cupcake Sales')

# function to show the plot
graph.show()
