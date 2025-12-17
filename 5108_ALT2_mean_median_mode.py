# 5108 Functions for ALT2
# G Hennessy CUS

def getFreqDist(listIn): 
    # Initialise 2 empty lists which will look
    # like 2 rows of a frequency distribution
    valuesList=[]
    freqList=[]
    # Loop through the data adding new values and freqs
    for value in listIn:
        if value not in valuesList:
            valuesList.append(value)
            freqList.append(listIn.count(value))
    print("Values :",valuesList)
    print("Freqs  :",freqList)
    return valuesList, freqList

def findMean(listIn):
    # Find the sum of elements
    total=sum(listIn)
    # divide by number of elements
    meanValue=total/len(listIn)
    return meanValue
def findMedian(listIn):
    # Sort the list
    listIn.sort()
    # Check if list length is odd
    if len(listIn) %2 != 0: # It is odd
        pos = (len(listIn)+1)/2
        # Adjust for list index (starts at 0)
        pos -=1
        medianValue=listIn[int(pos)]
    else: # even
        # 2 indexes I'm looking for are (n/2)-1 and n/2
        pos2=int((len(listIn)/2))
        pos1=pos2-1
        
        print("In median: pos1 and pos2 are",pos1,pos2)
        medianValue=findMean(listIn[pos1:pos2+1])
        # or you could just use (n+1)/2 and then +/- 0.5
        # to find the two values
        # remember to -1 from both to turn them into indices
        # remember to convert them from floats to integers
    return medianValue

def findMode(listIn):
    # Sort the list
    listIn.sort()
    
    # Call the freq distribution creator
    vals, freqs = getFreqDist(listIn)
    
    # Find the value with highest frequency
    highestVal = max(freqs)
    # Find where that value is in the list
    pos = freqs.index(highestVal)
    # Find which value corresponds to that
    modalValue = vals[pos] 
  
    
    return modalValue

# Initialise a list
numList=[4,2,3,1,9,7,5,10]
#numList=[14.2234243,23.2313,31.2342342342]
mean = findMean(numList)
print("The mean is",mean)
median = findMedian(numList)
print("The median is",median)

#data=[2,2,3,1,4,5,2,1,1,1,1,1,1]
data=["Luas","Dart","Bike","Walk","Car","Luas","Dart","Luas","Bike","Walk","Car""Bike","Walk","Car","Dart","Luas","Dart","Dart","Luas","Dart","Dart","Luas","Dart"]
mode = findMode(data)
print("The mode is",mode)








