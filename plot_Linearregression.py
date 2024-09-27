# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 21:57:12 2024

@author: tamil
"""
import matplotlib.pyplot as plt

# Data
temperature = [30, 18, 36, 24, 15, 33, 21, 27]
ice_cream_sales = [500, 150, 800, 300, 100, 650, 200, 400]



# Set the figure size (width, height in inches)
plt.figure(figsize=(10, 6))
# Create a scatter plot
plt.scatter(temperature, ice_cream_sales, color='blue', marker='o')

# Add labels and title
plt.xlabel('Temperature (°C) Feature')
plt.ylabel('Ice Cream Sales (units sold) Label')
plt.title('Ice Cream Sales vs Temperature')

# Show the plot
plt.grid(True)
plt.show()




