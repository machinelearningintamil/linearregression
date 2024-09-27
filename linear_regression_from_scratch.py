# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 22:19:34 2024

@author: tamil
"""
import numpy as np
import matplotlib.pyplot as plt

# Data (Temperature and Ice Cream Sales)
temperature = np.array([30, 18, 36, 24, 15, 33, 21, 27])
ice_cream_sales = np.array([500, 150, 800, 300, 100, 650, 200, 400])

# Function to calculate the slope (m) and intercept (b) of the linear regression line
def linear_regression(x, y):
    n = len(x)
    
    # Calculate the means of the x and y data
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    # Calculate the slope (m)
    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)
    m = numerator / denominator
    
    # Calculate the intercept (b)
    b = y_mean - (m * x_mean)
    
    return m, b

# Perform linear regression
m, b = linear_regression(temperature, ice_cream_sales)

# Predict ice cream sales based on temperature using the calculated slope and intercept
predicted_sales = m * temperature + b

# Plot the data points (scatter plot)
plt.figure(figsize=(10, 6))
plt.scatter(temperature, ice_cream_sales, color='blue', marker='o', label='Actual Data')

# Plot the linear regression line
plt.plot(temperature, predicted_sales, color='red', label='Fitted Line')

# Add labels and title
plt.xlabel('Temperature (°C) Feature')
plt.ylabel('Ice Cream Sales (units sold) Label')
plt.title('Linear Regression from Scratch: Ice Cream Sales vs Temperature')

# Show legend and grid
plt.legend()
plt.grid(True)
plt.show()

# Print the slope and intercept
print(f"Slope (m): {m}")
print(f"Intercept (b): {b}")
