# This code allows the user to set up a list of lists
# At the end, it should look like this
# outerList = [['Maths','H','78'],['French','H','82'],['Biology','O','62']]
# Initialise the outer list
outerList=[]


# Set up a loop - we'll start with 3 elements in the outerList
for i in range(3):
    # Initialise the inner list (must be done inside loop - otherwise we just keep appending!
    innerList=[]
    # Get user to input 3 values and append these to the innerList
    subject=input("Enter subject :")
    level=input("Enter level :")
    percent=input("Enter percentage achieved :")
    innerList.append(subject)
    innerList.append(level)
    innerList.append(percent)
    # now add my completed innerList to my outerList
    outerList.append(innerList)
    
print(outerList)
    
