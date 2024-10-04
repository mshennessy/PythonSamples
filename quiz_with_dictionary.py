# G Hennessy CUS
# Countries and capitals quiz using Python Dictionaries

# Set up dictionary
# dict = { key:value, key: value ...}
capitalsDict={
    "Ireland":"Dublin",
    "France":"Paris",
    "Germany":"Berlin"
}

# Add an entry to the dictionary
capitalsDict.update({"UK":"London"})

print (capitalsDict)
# remove an entry from the dictionary
capitalsDict.pop('France')

print (capitalsDict)

# Go through each dicionary pair
for country, capital in capitalsDict.items():
    ans = input("What is the capital of "+ country)
    if ans == capital:
        print("Well done")
    else:
        print("Incorrect")

print("Keys :",capitalsDict.keys())



# Note that dictionary structure is very flexible
# Doesn't have to be all strings
randomDict={
    1:"One",
    "Three":3,
    "A":7000,
    'N':"W"
    }

for a, b in randomDict.items():
    print ("a is ",a, "and b is ",b)