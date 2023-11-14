def mySort(listIn):
    if len(listIn)>1:
        #pivot=listIn[0]
        pivot=listIn[len(listIn)-1]
        print("Pivot",pivot)
        belowPiv = []
        abovePiv = []
        for item in listIn[:len(listIn)-1]:
            if item < pivot:
                belowPiv.append(item)
                print("\tbelow", item)
            else:
                abovePiv.append(item)
                print("\tabove", item)
        return mySort(belowPiv) + [pivot] + mySort(abovePiv)
    else:
        return listIn
    
myList =  [45, 31, 64, 92, 50, 24, 39, 11, 4, 76, 83]

print ("Sorted list: ", mySort(myList))