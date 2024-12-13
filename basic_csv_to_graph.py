# G. Hennessy
# Sample code to open a CSV file and produce a graph

import csv							# library to handle CSV
import matplotlib.pyplot as plt		# for plotting graphs

# Initialize lists for data from the CSV file
countries = []
medals = []

# Open the CSV file using standard file open function
f = open('medals.csv', 'r')
# New method: using a special CSV reader which takes care
# of all the formatting issues such as \n etc
csv_reader = csv.DictReader(f)
# For loop which processes the object csv_reader row by row
for row in csv_reader:
    countries.append(row['Country'])
    medals.append(int(row['Medals']))  # Convert medals to integer
# Close the file
f.close()

print("Countries list:",countries)
print("Medals list:",medals)
# Create a pie chart using matplotlib
plt.figure(figsize=(8, 8))
# pie chart : numbers, sector names, num decimal places,angle
plt.pie(medals, labels=countries, autopct='%1.1f%%', startangle=0)
plt.title('Medals Distribution by Country')
# Optional saving my graph in a .png file
plt.savefig('medalsPie.png')
plt.show()
