# G Hennessy CUS
# This code runs through a list of lists and sorts it based on the
# 2nd element of the inner list
# Random test data
listOfLists=[[5,62,31],[1,97,7],[3,0,3],[1,56,3],[5,56,3],[95,5,3]]
#Make a copy of the list so that I can remove the highest value
#and sort the remainder of the list
copyList=listOfLists.copy()
#Create an empty list to append the max value list to on each pass
sortedList=[]
# We will test item 2 in the list ie index [1] and compare it to maxVal
maxVal=0
# Place holder for the list containing the maxVal
maxList=[]

# For each list in the original master list (note, this list never changes)
for i in range(len(listOfLists)):
    # Now we are working through the lists in the copied version
    for aList in copyList:
        # Check if the value is the highest so far and save the list with the highest value
        if aList[1] >= maxVal:
            maxVal = aList[1]
            maxList=aList
    # Show the highest (remove this later) and append to our new sorted list
    print("Highest is",maxList)
    copyList.remove(maxList)
    sortedList.append(maxList)
    # Reinitialise maxval for next pass
    maxVal=0

print("Sorted",sortedList)

    