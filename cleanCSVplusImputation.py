# Pre-processing data
# G. Hennessy CUS
# You should have a csv file called "dirty.csv" with at least
# two columns headed "Surname" and "Cost". Enter some surnames
# that contain spaces and or apostrophes in the surname column.
# Enter numeric values that have lots of decimal places in the
# cost column.
# You should leave some of the values blank to test imputation
# You can amend this code to do the pre-processing for your ALT2
# or coursework projects.

import csv

# Read data from dirty.csv and process it
# (Using with open here) - if you just use open() remember to close()
# the files also

with open('dirty.csv', 'r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    # Prepare the field names for the output file. These will need to be written to the cleaned file.
    fieldnames = reader.fieldnames
    # This list is needed to keep a record of all cleaned rows as we need to write it all in one go
    # at the end (unlike earlier version where we wrote a row at a time.
    outputData=[]
    # This list is for keeping track of all numeric values, in case you need to use imputation
    costValues=[]
    
    for row in reader:
        # Check for empty cost rows and relace blanks with a mean value
        if row["Cost"] != "":
            # Process "Cost" column - round all values to 2 decimal places
            # Note all data read from CSV is type string, so cast it to
            # a float before you round
        
            row["Cost"] = round(float(row["Cost"]),2)
            costValues.append(row["Cost"])
            
        # Process "Surname" column
        # Get rid of blanks and then spaces
        row["Surname"] = row["Surname"].replace(" ", "")
        row["Surname"] = row["Surname"].replace("'", "")

        outputData.append(row)

# Calculate the mean cost value to replace blanks with
meanCost= round(sum(costValues)/len(costValues),2)
# Now go through the data a second time, performing imputation if needed
for row in outputData:
    # Check for empty cost rows and relace blanks with a mean value
    if row["Cost"] == "":
        row["Cost"]=meanCost

# Open the output file
with open('clean.csv', 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()  # Write header to the clean file
    # note writerows() plural (as we are not writing a row at a time in this version
    writer.writerows(outputData)

print("Data cleaning (with imputation) complete. Cleaned data saved to clean.csv.")