# Sample code for a pygal interactive graph
# Importing pygal did cause some problems with old versions of python
# This code my require re-installing Thonny or upgrading Python to > 3.8
# G Hennessy CUS

import csv
import pygal

# Read data from CSV
csv_file = "7610_CAOshort.csv"
hours= []
points = []


with open(csv_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Add data from CSV columns to our lists
        hours.append(float(row["Hours of study"]))
        points.append(float(row["CAO points"]))

# Create a scatter plot. Without stroke=False, the dots are joined for some reason
scatter_plot = pygal.XY(stroke=False,title="Scatterplot: Hours of Study vs CAO Points")
scatter_plot.x_title = "Hours of Study"
scatter_plot.y_title = "CAO Points"

# Add data to the plot. The zip functions 
scatter_plot.add("Data Points", list(zip(hours, points)))

# Save the plot to an SVG file
scatter_plot.render_to_file("myScatter.svg")

print("Created scatterplot - see myScatter.svg and use embed to view the file from your report html")