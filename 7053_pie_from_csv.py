# Simple example o a pie chart from a csv file
# G Hennessy


import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('cars_new.csv')

# Count the occurrences of each car type
# This saves you looping through the data and counting
car_counts = df['car_type'].value_counts()

# Plot a pie chart
plt.figure(figsize=(8, 8))  # Optional: Set figure size
# car_counts.index is a pandas thing ... saves you having to make a list
plt.pie(car_counts, labels=car_counts.index)
plt.title('Distribution of Car Types')
plt.axis('equal')  # Equal aspect ratio ensures pie chart is circular.
plt.show()