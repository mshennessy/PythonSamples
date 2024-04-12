#Investigatin Code Efficiency
#You need to know about bigO notation for this.

# Import python time. We'll use .time() and .sleep() to add delays

import matplotlib.pyplot as plt
import random
import time

# Ask the user to control the delay. Try .01 of a second
delay=float(input("What delay would you like:"))


#-----------------------------------------------------------------------------------#
# O(n^2) (n squared) Try doubling the length of the list. Will the program take more
# than twice as long to run?
listA = [ 2, 3, 4]
print(" O(n^2) n-squared demo ...")
dataSize=[]
timeNeeded=[]

for j in [5,10,15,20,25,30]:
    listA=[]
    for i in range(j):
        listA.append(random.randint(1,10000))
    start = time.time()
    for i in listA:
        for j in listA:
            #print (i,j,"   ",end="")
            time.sleep(delay)
    end = time.time()
    print("\n O(n^2) - timing where n = ",len(listA), "Time taken was:",round((end-start)/delay,1),"seconds")
    print("\n\n")
    dataSize.append(len(listA))
    timeNeeded.append(round((end-start)/delay,1))

    print("\n\n")

print(dataSize)
print(timeNeeded)


# Creation of Data 

# Plotting the Data 
plt.plot(dataSize, timeNeeded, label='O(n^2) n-squared') 
 
plt.xlabel('n') 
plt.ylabel('time (s)') 
plt.title("O(n^2) n-squared demo") 
plt.show()