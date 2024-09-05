# This code demonstrates how to use a list of lists
# This list is hardcoded for the exercise
outerList = [['Maths','H',78],['French','H',92],['Biology','O',62],['History','H',71]]



# Loop through each entry in the outer list
for subjList in outerList:
    print(subjList)
    for element in subjList:
        print(element)
    
    
# Ex 1:
# We have set up our list so that we the score is always the 3rd element
# Add code here to calculate the mean score


# Ex 2:
# Add code here to inform the user how many H and O subects they are taking

# Ex 3:
# It is decided that every student will get an extra 10% in every subject to a max of 100%
# Write code to adjust the score for each subject (round to nearest %) and
# print out the new scores like this
# Subject	Level	Adjusted Score
# Maths		H		86
# French etc


