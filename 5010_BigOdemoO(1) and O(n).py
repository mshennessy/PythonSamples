#Investigatin Code Efficiency
#You need to know about bigO notation for this.
# Import python time. We'll use .time() and .sleep() to add delays

import matplotlib.pyplot as plt
import random
import time
# Ask the user to control the delay. Try .1 of a second
print("This code uses a delay so that we can see the pattern of Big(O) efficiency")
print("If you set the delay to 1, you might be waiting a while")
print("Recommend setting it to 0.1 or even 0.01")
delay=float(input("What delay would you like:"))

#-----------------------------------------------------------------------------------#
# O(1) - can't simulate. size of data n doesn't effect the length of time to run the program.
# Think of posting a USB stick - full or empty, it takes the same length of time regardless of n
print(" O(1) .... ¯\_(ツ)_/¯\n\n")
#-----------------------------------------------------------------------------------#

# O(n) - the bigger n is, the longer the code takes to run, in direct proportion
print(" O(n) demo ...")
listA=[1,2,3] #,4,5,6,7,8,9,10]


dataSize=[]
timeNeeded=[]

# This test code sets up lists with 10, 20 ... 80 elements and performs a search on each one
for j in [10,20,30,40,50,60,70,80]:
    listA=[]
    for i in range(j):
        # Add a random number to the list
        listA.append(random.randint(1,j))
    
    #Search for a value that may be in the list
    searchItem=random.randint(0,j-1)  # eg if j was 10, values in list will be 0...9
    start = time.time()
    for i in listA:
        if i == searchItem:
            print("Found",j)
            # Try commenting out this break
            # It is only necessary if you are looking for just
            # the first instance of the search_item
            break
        time.sleep(delay)
    end = time.time()
    print("\n O(n) - timing where n = ",len(listA),"Time taken was:",round((end-start)/delay,1),"seconds")
    print("\n\n")

    dataSize.append(len(listA))
    timeNeeded.append(round((end-start)/delay,1))

    print("\n\n")

print(dataSize)
print(timeNeeded)


# Creation of Data 

# Plotting the Data 
plt.plot(dataSize, timeNeeded, label='O(n)') 
 
plt.xlabel('n') 
plt.ylabel('time (s)') 
plt.title("O(n) demo") 
plt.show()
