dataFile = open("customer_shopping_data-large.csv", 'r')
for line in dataFile:
    values = line.split(',')
for value in values:
    print(value)