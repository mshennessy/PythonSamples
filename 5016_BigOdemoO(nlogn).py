#Investigatin Code Efficiency
#You need to know about bigO notation for this.

import matplotlib.pyplot as plt
import random
import time

#-----------------------------------------------------------------------------------#

# O(nlog n) - quicksort is good example
# Function to find the partition position
print(" O(n log n) demo ...")
def partition(listIn, low, high):

    # choose the rightmost element as pivot
    pivot = listIn[high]
    # pointer for greater element
    i = low - 1 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):

        if listIn[j] <= pivot:
            #time.sleep(delay)
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
            # Swapping element at i with element at j
            (listIn[i], listIn[j]) = (listIn[j], listIn[i]) 
    # Swap the pivot element with the greater element specified by i
    (listIn[i + 1], listIn[high]) = (listIn[high], listIn[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort
def quickSort(listIn, low, high):

    #print("Called quicksort")
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pivot = partition(listIn, low, high)
        # Recursive call on the left of pivot
        quickSort(listIn, low, pivot - 1)
        # Recursive call on the right of pivot
        quickSort(listIn, pivot + 1, high)
    else:
        # exit criteria
        return
dataSize=[]
timeNeeded=[]
# above 262144 exceeds recursion limit
for j in [1,2,4,8,16,32,64,128,256,512,1024,2046,4096,8192,16384,32708,65536,131072,262144]:

    listA=[]
    for i in range(j):
        listA.append(random.randint(1,10000))
        #listA.append(1000-i) # create a worst case scenario
        #print(listA)
    #listA = [6,99,2,65,28,87,24,1,89,32,54,78,53,11,77,41,100,87,83,78,75,72,69,66,63,62,61,58,54,52,48,1]
    #listA=[100,87,83,78,75,72,69,66,63,62,61,58,54,52,48,1]
    #listA=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    #listA=[4,2,3,1,6,8,5,11]
    #print("Unsorted List:", listA)
    start = time.time()
    quickSort(listA, 0, len(listA)-1)
    print('Sorted List:',listA)
    end = time.time()

    print("\n O(nlog n) - timing where n = ",len(listA), "Time taken was:",round(end-start,5),"seconds")
    dataSize.append(len(listA))
    timeNeeded.append(round(end-start,5))

    print("\n\n")

print(dataSize)
print(timeNeeded)


# Creation of Data 

# Plotting the Data 
plt.plot(dataSize, timeNeeded, label='O(n log n) baby!') 
 
plt.xlabel('n') 
plt.ylabel('time (s)') 
plt.title("n log n demo") 
plt.show()
