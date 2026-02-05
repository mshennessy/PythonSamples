# Pre-processing data
# G. Hennessy CUS
#Simplified version of imputation demo


values= [123,654,787,334,789,0,1223,546,345,82]
clean_values=[]

print("Before Imputation:",values)

# Go through the values list, adding non-zero values
# to a new list
for i in range(len(values)):
    if values[i] != 0:
        clean_values.append(values[i])
#Now find the mean of the list (call your findMean function)
meanValue=round(sum( clean_values)/len(clean_values))

# Now go through your list of values again, replacing
# blanks with mean
for i in range(len(values)):
    if values[i] == 0:
        values[i]=meanValue
        

print("After Imputation:",values)