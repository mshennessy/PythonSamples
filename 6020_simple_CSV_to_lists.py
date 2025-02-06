# Model code to read data from a CSV file columns into a list
# G Hennessy CUS

# Using only simple CSV module (no pandas)
import csv

# Initialize empty lists
kmsList = []
yearList = []
modelList = []

# Read the CSV file - this should be pre-processed code
with open('cars.csv') as file:
    reader = csv.DictReader(file)

    # Add to our lists for each row
    for row in reader:
        kmsList.append(int(row['Kms']))  # Convert to integer for numeric values
        yearList.append(int(row['Year']))  # Convert to integer for numeric values
        modelList.append(row['Model'])  

# Print the extracted lists
print("Kms:", kmsList)
print("Year:", yearList)
print("Model:", modelList)