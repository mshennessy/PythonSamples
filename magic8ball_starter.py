# Magic 8Ball starter code
# G. Hennessy CUS

# Import a library that will do the random part
from random import randint

# Set a Boolean variable to True
keepPlaying = True

while (keepPlaying):   # This will run forever unless we make keepPlaying = False somwehere ...
    # ask the user for input
    question = input ("ask the magic 8-ball question")
    #generate a random number, because it isn't actually magic
    #this generates a number between 1 and 2 inclusive (change to e.g. (1,6) for a die)
    randNum=randint(1,2)
    #add a check in here for if the user hasn't entered a question
    #this is the signal to end the magic 8-ball game
    if randNum == 1:
        print("Outlook not so good")
    #Add some other options here. Remove the # from the next two lines and repeat them
    #elif randNum == 2:
        #print("Possible")
    else:
        print("Definitely!")
        
#Note that the next line is outside the while loop as it is not indented
print("Thanks for playing")