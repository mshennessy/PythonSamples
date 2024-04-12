# LPT 5310 Home-made stats functions
# My own functions for frequency, mode, median and mean
# We are assuming that the data we are analysing contains
# values 1 to 10 only (until step 5 on worksheet)

def findFreqAndMode(numsList):
    #Create a frequency table
    #Hint create a list of values and a list of frequencies
    #Find the mode (it doesn't matter if there are two or more modes)
    print("Finding frequency and mode",numsList)
    valueList=[1,2,3,4,5,6,7,8,9,10]
    freqList=[]
    for num in valueList:
        # Use the count() method to find the frequency of each value
        #
        pass
    print(valueList)
    print(freqList)
    #Now find the mode
    # return the mode
 

def findMean(numsList):
    #Find the mean of the data
    print("Finding mean")
    # return the mean value
    
def findMedian(numsList):
    #Find the median of the data (handle an odd number and even number in list)
    print("Finding median")
    # return the median value

    
    
#test data we will use
myList=[3,7,6,1,7,5,8,7,10,5,8,10,9,3,7,2,9]

mode=findFreqAndMode(myList)
    
median=findMedian(myList)
   
mean=findMean(myList)

print("Mode is",mode,"\tMedian",median,"\tMean",mean)


