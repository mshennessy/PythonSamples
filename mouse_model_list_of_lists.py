# Model with lists of lists
import random
# Allow output to have a background colour
from colorama import Back

import time # going to use this for a sleep

# Data structure used is a list of lists
# Main list is the current population of mice
# Each element of the main list is a sublist with this structure
# gender M/F, age (months), colour, state (fertile/pregnant), duration (used for reproduction)
# Names for indices into mouse list
GENDER=0
AGE=1
COLOUR=2
STATE=3
DURATION=4

# Values for state
INFERTILE=0
FERTILE=1
PREGNANT=2
# Values for duration
NOTRELEVANT=0
NOTREADY=1
READY=2


def createMouse(mumColour,dadColour):
    mouseAge = 0
    mouseGender = random.choice(['M','F'])
    mouseColour = random.choice([mumColour,dadColour])
    newMouse=[mouseGender,mouseAge,mouseColour,INFERTILE,NOTRELEVANT]
    return newMouse

def addOneMonth(currentPopulation,lifespan):

    print("Aging one month")
    # Check for old mice - 50% chance of death if > 5 months
    for mouse in currentPopulation:
        # If gestation period reached, produce baby mice
        if (mouse[DURATION] == 2):
            mouse[DURATION] = 0
            for i in range(1,random.randint(1,6)):
                createMouse(mouse[COLOUR],random.choice(["Black","Grey","White"]))
            mouse[STATE]=FERTILE
        # Roll on gestation period of pregnant mice
        if (mouse[STATE] == PREGNANT):
            mouse[DURATION] += 1
        # Mice become fertile above 2 months
        if (mouse[STATE] == INFERTILE) and (mouse[AGE] == 2):
            mouse[STATE] = FERTILE
        # Add one month to all mice
        mouse[AGE] += 1
        # A mouse might die after 10 months
        if (mouse[AGE] > lifespan):
            rollDiceOfDeath = random.randint(1,6)
            if rollDiceOfDeath >4:
                print("Death of mouse occurs")
                currentPopulation.remove(mouse)

    #print(currentPopulation)

def procreateMice(currentPopulation):
    for mouse in currentPopulation:
        if mouse[GENDER] == 'F' and mouse[STATE] == FERTILE:
            roleThePregnancyDice=random.randint(1,6)
            if roleThePregnancyDice > 4:
                print("Pregnancy occurs",'\a')
                #time.sleep(1)
                mouse[STATE] = PREGNANT
        if mouse[GENDER] == 'F' and mouse[STATE] == PREGNANT and mouse[DURATION] == READY :
            litterSize=random.randint(5,10)
            print("Producing",litterSize,"babies")
            for i in range(litterSize):
                currentPopulation.append(createMouse(mouse[COLOUR],random.choice(["Black","Grey","White"])))
            mouse[STATE] = FERTILE

def displayMousePopulation(pop):
    for mouse in pop:
        if mouse[GENDER] == "F":
            print(Back.RED, mouse[AGE],Back.WHITE," ",end= '')
        else:
            print(Back.BLUE, mouse[AGE],Back.WHITE," ",end= '')
    print(Back.WHITE,"")
   
def tallyMousePopulation(pop):
    #This function prints out a tally of the current mouse population
    # Number of females (of which infertile/fertile/pregnant) and males
    femaleCount=0
    maleCount=0
    infertileFemale=0
    fertileFemale=0
    pregnantFemale=0
    for mouse in pop:
        if mouse[GENDER] == "F":
            femaleCount+=1
            if mouse[STATE] == INFERTILE:
                infertileFemale +=1
            elif mouse[STATE] == FERTILE:
                fertileFemale +=1
            else:
                pregnantFemale +=1
        else:
            maleCount+=1
    print("Females     fertile      infertile      pregnant        Males     TOTAL")
    print(femaleCount," "*10,fertileFemale," "*10,infertileFemale," "*10,pregnantFemale," "*10,maleCount," "*10,len(pop) )


print("Welcome to the mouse simulation")
startingPop=int(input("How many mice do you wish to start with?"))
lifeExpectancy=int(input("what is the life expectancy in months?"))
simLength=int(input("How many months simulation:"))
outputChoice=int(input("Dispay mouse population (1) or just tallies (2)"))
# initialise my population based on user input
population=[]
for i in range(startingPop):
    population.append(createMouse(random.choice(["Black","Grey","White"]),random.choice(["Black","Grey","White"])))
   
print(population)

for i in range (simLength):
    print("MONTH: ",i+1)
    print("===========")
    addOneMonth(population,lifeExpectancy)
    procreateMice(population)
    #print(population)
    if outputChoice == 1:
        displayMousePopulation(population)
    else:
        tallyMousePopulation(population)
    #print("We have", len(population),"mice!!")



