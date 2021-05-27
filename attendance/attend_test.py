from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Distribution of grades: 
# 0 - 49  F
# 50 - 59 C
# 60 - 69 B
# 70+ - A

# Import the data and extract the grades
f = open('sample500.csv')
content = f.readlines()
f.close()

# Storage for distribution of grades: dictionary
grades = {
    'A': 0,
    'B': 0,
    'C': 0,
    'F':0
}

# Loop through all the lines in the list
for row in content:
    columns = row.split(',')
    marks = int(columns[-1])

    # Data cleaning for non attendance
    if int(columns[-1]) == 0:
        content.remove(row)
    else:

        # Count the grade
        if marks >= 70:
            grades['A'] += 1
        elif marks >= 60:
            grades['B'] += 1
        elif marks >= 50:
            grades['C'] += 1
        else:
            grades['F'] += 1

print(grades)

# Transforming the data for visualisation
keys = grades.keys()
values = []
for k in keys:
    values.append(grades[k])

# Bar chart visualisation
# Data ready for visualisation
x = np.array(list(keys))
y = np.array(values)

plt.bar(x,y)
plt.show()

# Pie chart visualisation
plt.pie(y, labels=list(keys))
plt.show()

# Delve deeper into attendance data
attend_grade = []

for row in content:
    # All the elements
    cols = row.split(',')

    # Extract elements
    student_id = cols[0]
    grade = int(cols[-1])
    attend = cols[1:-1]

    attend_rate = attend.count('X') / len(attend) * 100

    # Add the value pair to attend_grade
    # As a tuple
    attend_grade.append((attend_rate, grade))

# Sort by x (attendance rate)
attend_grade.sort()

# We need two separate lists for X and Y so we split the tuples
# again after sorting the list
rates_list = []
grades_list = []
for pair in attend_grade:
    rates_list.append(pair[0])
    grades_list.append(pair[1])

x = np.array(rates_list)
y = np.array(grades_list)

plt.scatter(x,y)
plt.show()

# Establish relationship between attendance rate
# And grade

x_reg = x.reshape((-1,1))
model = LinearRegression()
model.fit(x_reg, y)

# Data for the predictive model
r_sq = model.score(x_reg, y)
intercept = model.intercept_
coef = model.coef_

# Display model data
print('R-Squared: ', r_sq)
print('Intercept', intercept)
print('Slope: ', coef)

def predict(x):
    return x * coef + intercept

x_plot = np.array([0, 50, 100])
y_plot = np.array([predict(0), predict(50), predict(100)])

plt.scatter(x,y)
plt.plot(x_plot, y_plot, color='red')
plt.show()

# Do some predictions
x_in = 0
while x_in != -1:
    x_in = int(input('Please enter an estimated attendance'))
    predicted_result = predict(x_in)
    print('The predicted grade is: ', predicted_result)