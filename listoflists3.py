# G Hennessy CUS
# Sample code - how to set up and use a 2 dimensional array (list)
# Set up my list of lists (note each sublist has to have the same
# structure
allData=[[2,4,7,"M"],[1,3,5,"M"],[1,4,1,"F"],[1,3,5,"M"],[1,2,1,"M"],[1,1,5,"M"],[1,4,4,"F"],[4,1,5,"F"],[2,4,1,"M"]]

# Show the data as a  dimensional array 
for oneData in allData:
    for x in oneData:
        print (x, " ", end = "")
    print()

# Demo of how to index straight into one element
# Think of this like an excel spreadsheet where each
# cell has a coordinate such as A1 or D7
# Note that "row 3" here means the third row which
# has index 2 as we count from zero
print("row 3, element 4 :",allData[2][3])
