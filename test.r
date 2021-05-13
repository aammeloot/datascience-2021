# Predict weight based on height

# Vector: height of people in cm
h <- c(151,174,138,186,128,136,179,163,152,131)
# Vector: weight of the same people in kg
w <- c(63,81,56,91,47,57,76,72,62,48)

# Linear regression
# Find relation of weight / height
relation <- lm(w~h)

print(summary(relation))

plot(h, w, col="Blue", main="Height and Weight", abline(relation))
