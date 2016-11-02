__author__ = 'Tamby Kaghdo'

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import math

#load auto-mpg.data
columns = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model year", "origin", "car name"]
cars = pd.read_table("./data/auto-mpg.data", delim_whitespace=True, names=columns)
print(cars.head(5))

#explore some weight and mpg
fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
cars.plot("weight", "mpg", kind='scatter', ax=ax1)
cars.plot("acceleration", "mpg", kind='scatter', ax=ax2)
plt.show()

#fit a linear regression model with x=weight, y=mpg
lr = LinearRegression()
lr.fit(cars[["weight"]], cars["mpg"])

#create prediction of mpg based on weight
predictions = lr.predict(cars[["weight"]])
print(predictions[0:5])
print(cars["mpg"].head(5))

#plot the model
plt.scatter(x=cars["weight"],y=cars["mpg"], c="red")
plt.scatter(x=cars["weight"],y=predictions , c="blue")
plt.show()

#errors
mse = mean_squared_error(cars["mpg"],predictions )
rmse = math.sqrt(mse)
print("MSE: {0}").format(mse)
print("RMSE: {0}".format(rmse))


# *** explore horsepower and mpg ***

#filter out '?' and create a new data frame
filtered_cars = cars[cars["horsepower"] != '?']
#convert to numeric
filtered_cars["horsepower"] = filtered_cars['horsepower'].astype('float')
print(filtered_cars.head(5))

#plot horsepower, wight and mpg
fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.scatter(filtered_cars['horsepower'], filtered_cars['mpg'], c='red')
ax2.scatter(filtered_cars['weight'], filtered_cars['mpg'], c='blue')
plt.show()

#fit the model for the input horsepower
lr = LinearRegression()
lr.fit(filtered_cars[["horsepower"]], filtered_cars["mpg"])
#create mpg predictions
predictions = lr.predict(filtered_cars[["horsepower"]])
print(predictions[0:5])
print(filtered_cars["mpg"].head(5))

#plot the predictions
plt.scatter(x=filtered_cars["horsepower"],y=filtered_cars["mpg"], c="red")
plt.scatter(x=filtered_cars["horsepower"],y=predictions , c="blue")
plt.show()

#errors
mse = mean_squared_error(filtered_cars["mpg"],predictions )
rmse = math.sqrt(mse)
print("MSE: {0}").format(mse)
print("RMSE: {0}".format(rmse))

