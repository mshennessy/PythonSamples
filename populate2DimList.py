from random import randint

#Simple code to populate a 2 dimensional list
#Each sublist will contain a name followed by 5 (hardcoded) random numbers
def pop2DimList(num):
    list2d=[]
    # num is the number of players
    for i in range (num):
        list1d=[]
        name=input("Enter name")
        list1d.append(name)
        print("Choosing your numbers....")
        for i in range(5):
            list1d.append(randint(1,6))
        # Add to my 2 dimensional list
        list2d.append(list1d)
    return list2d

validValue= False
allPlayers=[]
#This code will prevent user from entering a letter or value outside range
while not validValue:
    count=input("Enter the number of players")
    if count.isdigit():
        numcount=int(count)
        if numcount > 1 and numcount < 10:
            validValue=True
    if not validValue:
        print("must be numeric and between 1 and 10")
# Call the function which populates the list
allPlayers=pop2DimList(numcount)
print(allPlayers)

#Now to use values in the list
#eg the 3rd person in the list (assume >= 3 for count)
#to print their name and the third number they rolled would be
print(allPlayers[2][3])