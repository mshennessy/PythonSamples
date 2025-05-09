#Investigatin Code Efficiency
#You need to know about bigO notation for this.

# Import python time. We'll use .time() and .sleep() to add delays

import matplotlib.pyplot as plt
import random
import time
# Ask the user to control the delay. Try .1 of a second
delay=float(input("What delay would you like:"))

#
# O(n!) Warning ... make your list shorter here!
# create a list with all permutations of list B elements (which will be 4! options)
print(" O(n!) demo ...")
# Python function to print permutations of a given list
def permutation(listIn):
    # If lst is empty then there are no permutations
    if len(listIn) == 0:
        return []
    # If there is only one element in lst then, only
    # one permutation is possible
    if len(listIn) == 1:
        return [listIn]
    # Find the permutations for lst if there are
    # more than 1 characters
    perm = [] # empty list that will store current permutation
    # Iterate the input(lst) and calculate the permutation
    for i in range(len(listIn)):
        m = listIn[i]
        # Extract lst[i] or m from the list.  remList is remaining list
        remList = listIn[:i] + listIn[i+1:]
        # Generating all permutations where m is first element
        for p in permutation(remList):
            perm.append([m] + p)
    time.sleep(delay)
    return perm
 
listB = ['A','B','C','D','E','F','G']
start = time.time()
for p in permutation(listB):
    pass
    #print (p)
end = time.time()
print("\n O(n!) - timing where n = ",len(listB), "\nTime taken was:",round((end-start)/delay,1),"seconds")
