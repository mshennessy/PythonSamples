#This is a bubble sort - extremely inefficient
myList =  [5,3,1,9,8,2,4,7]

print ("unsorted : ",myList)
print ()

for item in range(len(myList)):
    print("New pass: ",myList)
    for index in range(len(myList)-1):
        print("          ",myList)
        if myList[index] > myList[index+1]:
            tempstore = myList[index]
            myList[index] = myList[index+1]
            myList[index+1] = tempstore
        
print ("sorted : ", myList)