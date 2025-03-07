# Oscar Analytics Example
# G Hennessy CUS

# CSV handling option 3 - using pandas

# For data analysis
import pandas as pd
# For a graph demo at the end
import matplotlib.pyplot as plt

# Note that with pandas we don't have to use a file open()
# Read from the csv file using pandas. Pandas returns a data structure
# called a dataframe df
df = pd.read_csv('oscar.csv')

# Example 1 - choosing your data
# For your analysis, you may need to isolate some specific data
# When there are multiple values you are isolating you
# must use & between them (not "and") It's a pandas thing.
# Eg Look for films that got more than 1 nomination in 2022
#    Create a sub-dataframe for this data
# Using .loc[]
subdf=df.loc[(df["Year"]==2022) & (df["NumberOfNominations"]>1)]
print("The movies that got more than 1 nomination in 2022\n", subdf)
#Total up the values in each column - no need for a for loop!
sumAwards = subdf["NumberOfAwards"].sum()
sumNoms = subdf["NumberOfNominations"].sum()
print("Total Awards",sumAwards,"and total nominations",sumNoms)

# Example 2 - choosing a row by index
# using .iloc[] to find a row by index (ie 0,1,2,3 ...)
print("Printing the 5th row for a demo",df.iloc[4])

# Example 3 - building up data for a subset of the dataframe
# Now try finding the average number of nominations per year from 1940 to 2022
# Prepare two lists, one for the year and one for the corresponding number
# of nominations that year
years=[]
nomsByYear=[]
for i in range(2020,2023):  # You can change years further back - it's a lot of data
    #print("-"*10,i,"-"*10)
    years.append(i)
    # define a new sub-dataframe for each year
    subdf=df.loc[df["Year"]==i]
    #print(subdf)
    nomsByYear.append(int(subdf["NumberOfNominations"].sum()))

#Showing data generated in previous lines
print("-"*30)
print("Years",years)
print("Nominations per year",nomsByYear)
print("-"*30)

# Example 4 - comparing data on the same row
# Go through the data and read corresponing values on a single row
# You need to use an index to keep track of the row you are on
""" Commented out as output takes ages
print("\n\nFilms that won every award they were nominated for:")
for x in range(len(df)): # note len() returns number of rows
    if df["NumberOfAwards"][x] == df["NumberOfNominations"][x]:
        print(df["Year"][x]," : ",df["Film"][x], "with",df["NumberOfNominations"][x],"nominations") 
"""
# Example 5 - making a graph directly from the data
# You can use an inbuilt pandas graph
df.plot.scatter(x='NumberOfNominations', y='NumberOfAwards')
# Or the standard matplotlib
plt.scatter(list(df["NumberOfNominations"]),list( df["NumberOfAwards"]))
plt.show()

# Example 6 - making a graph that requires some organisation of data
# We will graph the number of films that got 1, 2, 3 etc awards
# We'll need a list of all the different counts of awards. Find the max and then
# make a list of 0 up to the max.
maxAwards = df["NumberOfAwards"].max()
print(maxAwards)
awardsCount=[]
for i in range(maxAwards):
    awardsCount.append(i)  # will start with 0
awardsCount.append(maxAwards)  # make sure it goes 0 to maxAwards
# Now create a list of the number of films that got that many awards
moviesCount=[]
for award in awardsCount:
    subdf=df.loc[(df["NumberOfAwards"]==award)]
    moviesCount.append(len(subdf))
# Think of these 2 lists as the 2 rows of a frequency distribution in maths
print("Two lists ready for a graph",)
for i in awardsCount:  
    print("Count:", awardsCount[i], "Freq", moviesCount[i])

# Plot a bar chart. You might want to change the years to make
# the bar chart more meaningful
plt.bar(awardsCount, moviesCount)
plt.title('Number of awards in Oscars')
plt.xlabel('Award Count')
plt.ylabel('Frequency')
plt.show()

