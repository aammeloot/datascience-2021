from matplotlib import pyplot as plt
import numpy as np

# Loading dataset of used VW cars on the UK market
# From Kaggle

f = open("vw.csv")

# Creating 4 dictionaries
model = {}
year = {}
transmission = {}
fuel = {}

cur_line = f.readline()

while cur_line:
    # Split the current line into different elements
    elts = cur_line.split(',')

    # If the current model exists in the dictionary
    # Increment the count otherwise create the entry
    if elts[0] in model.keys():
        model[elts[0]] += 1
    else:
        model[elts[0]] = 1

    # Same with year
    if elts[1] in year.keys():
        year[elts[1]] += 1
    else:
        year[elts[1]] = 1

    # Transmission
    if elts[3] in transmission.keys():
        transmission[elts[3]] += 1
    else:
        transmission[elts[3]] = 1

    # Fuel
    if elts[5] in fuel.keys():
        fuel[elts[5]] += 1
    else:
        fuel[elts[5]] = 1

    # Read the next line
    cur_line = f.readline()

f.close()

# Extract the different types of fuel in arrays
fueltypes = []
fuelcounts = []


fueltypes = list(fuel.keys())
fueltypes.sort()
print(fueltypes)

for fl in fueltypes:
    fuelcounts.append(fuel[fl])

fig1, ax1 = plt.subplots()
explode = (0,0.1,0,0)
ax1.pie(fuelcounts, explode = explode, labels = fueltypes, startangle = 90, autopct = '')
plt.show()