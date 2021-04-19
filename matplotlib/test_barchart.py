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

# Visualisation of the different years
# First array = all the years

yeararray = list(year.keys())
# The years in order
yeararray.sort() # Sort in chronological order
print(yeararray)
yearcount = []

# For every single year
# Extract the number and put it into a 
# Sorted array
for y in yeararray:
    yearcount.append(year[y])
print(yearcount)

# Create an array of positions (l-r)
# for the X axis
positions = np.arange(len(yeararray))

# Create a bar plot
plt.bar(positions, yearcount)
plt.xticks(positions, yeararray)
plt.title("Volkswagen car available on the secondhand market")
plt.xlabel("Year")
plt.ylabel("Models available")

plt.show()
# print(model, year, transmission, fuel)

