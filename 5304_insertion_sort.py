# 1. Initialise an unsorted list
the_list = [5,3,1,9,8,2,4,7]
print("Before",the_list)
# 2. Initialise a marker
marker = 1 # Note, we start with 2nd element and compare with the first
# 3. Traverse through all list items
while (marker < len(the_list)):
    # 4. Insert the selected item to its correct position
    j = marker
    print("During",the_list,"marker is",the_list[j])
    while (the_list[j] < the_list[j-1] and j>0):
        tmp = the_list[j]              # Swap (use tmp as a temporary holding value)
        the_list[j] = the_list[j-1]
        the_list[j-1] = tmp
        print("     moving",tmp)
        j = j-1
    # 6. Advance the marker to the right by 1 position
    marker = marker+1
print("After",the_list)