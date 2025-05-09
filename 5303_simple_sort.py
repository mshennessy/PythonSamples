
# A Very Simple Sort v1
unsorted_list = [5,3,1,9,8,2,4,7] # the list to be sorted
sorted_list = [] # the initial (empty) sorted list
print("Before - Unsorted:",unsorted_list)
print("Before - Sorted:",sorted_list)
# Loop over every element in the unsorted list
for i in range(len(unsorted_list)):
    smallest = min(unsorted_list) # min returns the smallest
    sorted_list.append(smallest) # append the smallest to the sorted list
    unsorted_list.remove(smallest) # remove the smallest from unsorted_list
    print("   During - Unsorted:",unsorted_list)
    print("   During - Sorted:",sorted_list)
print("After - Unsorted:",unsorted_list)
print("After - Sorted:",sorted_list)