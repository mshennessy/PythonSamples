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
# O(log n) - only the binary search on our course
print(" O(log n) demo ...")
def binary_search(listIn, low, high, x):
    # For our timing and graphs
    time.sleep(delay)
    # Check base case
    if high >= low:
        mid = (high + low) // 2 # Use floor divide to avoid decimals
        # If element is present at the middle itself
        if listIn[mid] == x:
            return mid
        # If element is smaller than mid, then it can only
        # be present in left sublist
        elif listIn[mid] > x:
            return binary_search(listIn, low, mid - 1, x) 
        # Else the element can only be present in right sublist
        else:
            return binary_search(listIn, mid + 1, high, x)
    else:
        # Element is not present in the list
        return -1

dataSize=[]
timeNeeded=[]
# Test list - 8 elements
# Should take log(base2)8 which is 3 seconds.
# If you double the length of the list. Will it take twice as long?
for j in [1,2,4,8,16,32,64,128,256,512,1024,2046,4096,8192,16384,32768,65536]:
    listA=[]
    for i in range(j):
        # numbers in sequence (must be in order for binary search)
        listA.append(i)
    
    #Search for a value in the list (between 1 and length of list)
    searchItem = random.randint(1,j)
    # Try changing your searchItem to a value that cannot be in the list
    #searchItem=1000000
     
    start = time.time()
    # Start the search: pass the list, the index of the first element,
    # the index of the last element and the item we are searching for
    result = binary_search(listA, 0, len(listA)-1, searchItem)
    print(result)
    end = time.time()
    print("\n O(log n) - timing where n = ",len(listA), "Time taken was:",round((end-start)/delay,1),"seconds")
    print("\n\n")

    dataSize.append(len(listA))
    timeNeeded.append(round((end-start)/delay,1))

    print("\n\n")

print(dataSize)
print(timeNeeded)


# Creation of Data 

# Plotting the Data 
plt.plot(dataSize, timeNeeded, label='O(log n)') 
 
plt.xlabel('n') 
plt.ylabel('time (s)') 
plt.title("log n demo") 
plt.show()

