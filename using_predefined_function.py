# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 22:22:17 2024

@author: tamil
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
temperature = np.array([30, 18, 36, 24, 15, 33, 21, 27]).reshape(-1, 1)
ice_cream_sales = np.array([500, 150, 800, 300, 100, 650, 200, 400])

# Create and fit the linear regression model
model = LinearRegression()
model.fit(temperature, ice_cream_sales)

# Predict sales based on the temperature (for plotting the regression line)
predicted_sales = model.predict(temperature)

# Set the figure size
plt.figure(figsize=(10, 6))

# Scatter plot for original data
plt.scatter(temperature, ice_cream_sales, color='blue', marker='o', label='Actual Data')

# Plot the regression line
plt.plot(temperature, predicted_sales, color='red', label='Fitted Line')

# Add labels and title
plt.xlabel('Temperature (°C) Feature')
plt.ylabel('Ice Cream Sales (units sold) Label')
plt.title('Linear Regression: Ice Cream Sales vs Temperature')

# Show legend and grid
plt.legend()
plt.grid(True)
plt.show()