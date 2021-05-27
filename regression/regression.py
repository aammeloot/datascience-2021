import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

# Create x and y data to teach the model
xplot = np.array([5,15,25,35,45,55])
x = np.array([5,15,25,35,45,55]).reshape((-1,1))
y = np.array([5,20,14,32,22,38])

print(x)
print(y)

# Visualisation FYI
plt.scatter(xplot, y)


# Create the regression model
model = LinearRegression()
model.fit(x,y)

# Display the model
r_sq = model.score(x,y)
print('Coefficient of determination: ', r_sq)

print("Intercept: ", model.intercept_)
print("slope:", model.coef_)

# From model create an array of Ys using coef and intercept

yplot = []
for current_x in xplot:
    yplot.append(current_x * model.coef_ + model.intercept_)

yplot = np.array(yplot)

plt.plot(xplot, yplot)
plt.show()

def predict(x_val):
    print("Prediction for:", x_val,"--", x_val*model.coef_+model.intercept_)

vals_to_predict = list(range(0,500,10))

for v_p in vals_to_predict:
    predict(v_p)

