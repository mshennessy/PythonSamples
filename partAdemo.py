# Sample code for paper C part a showing multiple (but not all) options
# G Hennessy CUS

s=0
#sentence=input("Enter your sentence") # 
#For test: easier than typing in sentence each time
sentence="Splendid paper Cs 123!"

#ai first version --------------------------------
#count Ss
sLower=0
sUpper=0

# basic for loop, looping through characters in a string
for letter in sentence:
    print(letter)
    if letter == 's':
        sLower+=1
    elif letter == 'S':
        sUpper+=1
    else:
        pass
print("Total \"S\"s",sLower+sUpper)

#ai neater version --------------------------------
# basic for loop, looping through characters in a string
sCount=0
senLower=sentence.lower()
for letter in senLower:
    print(letter)
    if letter == 's':
        sCount+=1
    
print("Total \"S\"s",sCount)

# aii
# best way cos it practices "if in list"
vowelCount = 0        # Initialise vowel count
vowels=['a','e','i','o','u']
for letter in senLower:
    if letter in vowels:
        print("Vowel",letter)
        vowelCount+=1 # Increment vowel count
print("Total vowels",vowelCount)

#aii alternative but not recommended
aCount = senLower.count("a")
print(aCount)
#or quicker...
print("Total vowels",senLower.count("a")+senLower.count("e")+senLower.count("i")+senLower.count("o")+senLower.count("u"))
        
#iii
#print("A".isalpha())
letterCount = 0     # Initialise letter count
digitCount = 0     # Initialise digit count
for letter in senLower:
    if letter.isalpha():
        print("Got a letter", letter)
        letterCount+=1 # Increment letter count
    elif letter.isdigit():
        print("Got a digit", letter)
        digitCount+=1 # Increment digit count
    
print("Total letters",letterCount)
print("Total digits",digitCount)

#iv number of words
# count the spaces and then add 1
spaceCount=0
for letter in senLower:
    print(letter)
    if letter == ' ':
        spaceCount+=1

# allow for extra word after last space
spaceCount+=1
print("Total words",spaceCount)

# ------------------STARTING AGAIN -------------------
# This time we just loop through the characters in the
# sentence one time ... much more efficient
s=0
#sentence=input("Enter your sentence")
#Easier than typing in sentence each time
sentence="Splendid paper Cs 123!"

#ai neater version --------------------------------
# basic for loop, looping through characters in a string
sCount=0
senLower=sentence.lower()
print("Your sentence was",sentence)
print("Your lowercase sentence was",senLower)
# Nicer version - only loop through senLower ONCE!
vowels=['a','e','i','o','u']
# Initialise counters

for letter in senLower:
    print(letter)
    if letter == 's':     # i
        sCount+=1
    elif letter == ' ':   # iv
        spaceCount+=1
    elif letter in vowels: # ii
        print("Vowel",letter)
        vowelCount+=1 # Increment vowel count
    # Must be a separate if
    # iii
    if letter.isalpha():
        print("Got a letter", letter)
        letterCount+=1 # Increment letter count
    elif letter.isdigit():
        print("Got a digit", letter)
        digitCount+=1 # Increment digit count
    
print("Total S's",sCount)
print("Total vowels",vowelCount)
print("Total letters",letterCount)
print("Total digits",digitCount)
print("Total words",spaceCount + 1) 

