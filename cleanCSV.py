# Pre-processing data
# G. Hennessy CUS
# You should have a csv file called "dirty.csv" with at least
# two columns headed "Surname" and "Cost". Enter some surnames
# that contain spaces and or apostrophes in the surname column.
# Enter numeric values that have lots of decimal places in the
# cost column.
# You can amend this code to do the pre-processing for your ALT2
# or coursework projects.

import csv

# Read data from dirty.csv and process it
# (Using with open here) - if you just use open() remember to close()
# the files also

with open('dirty.csv', 'r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    # Prepare the field names for the output file
    fieldnames = reader.fieldnames

    # Open the output file
    with open('clean.csv', 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()  # Write header to the clean file

        for row in reader:
            # Process "Cost" column - round all values to 2 decimal places
            # Note all data read from CSV is type string, so cast it to
            # a float before you round
            row["Cost"] = round(float(row["Cost"]),2)

            # Process "Surname" column
            # Get rid of blanks and then spaces
            row["Surname"] = row["Surname"].replace(" ", "")
            row["Surname"] = row["Surname"].replace("'", "")

            # Write the cleaned row to the output file
            writer.writerow(row)

print("Data cleaning complete. Cleaned data saved to clean.csv.")