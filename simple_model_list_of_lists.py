# Model with lists of lists
import random

# Data structure used is a list of lists
# Main list is the current population of mice
# Each element of the main list is a sublist with this structure
# gender M/F, age (months), colour, state (fertile/pregnant)
# Names for indices into mouse list
GENDER=0
AGE=1
COLOUR=2
STATE=3


# Values for state. These will be used as indices into my list so
# we don't have to remember 
INFERTILE=0
FERTILE=1
PREGNANT=2



def createMouse(mumColour,dadColour):
    mouseAge = 0
    mouseGender = random.choice(['M','F'])
    mouseColour = random.choice([mumColour,dadColour])
    newMouse=[mouseGender,mouseAge,mouseColour,INFERTILE]
    return newMouse

def ageOneMonth(currentPopulation):

    # Check for old mice - 50% chance of death if > 5 months
    for mouse in currentPopulation:
        # Mice become fertile above 2 months
        if (mouse[STATE] == 0) and (mouse[AGE] == 2):
            mouse[STATE] = 1
        # Add one month to all mice
        print("Aging one month")
        mouse[AGE] += 1
        # A mouse might die after 10 months
        if (mouse[AGE] > 10):
            rollDiceOfDeath = random.randint(1,6)
            if rollDiceOfDeath >4:
                print("Death of mouse occurs")
                currentPopulation.remove(mouse)


def procreateMice(currentPopulation):
    for mouse in currentPopulation:
        if mouse[GENDER] == 'F':
            roleThePregnancyDice=random.randint(1,6)
            if roleThePregnancyDice > 4:
                print("Pregnancy occurs")
                mouse[STATE] = 2
                    
#initialise the populatation M/F, age, colour, status (1 = fertile), gestation count
population = [['F',6,"Grey",FERTILE],['F',10,"White",FERTILE],['M',4,"Grey",FERTILE],['M',9,"Black",FERTILE],['F',10,"Grey",FERTILE]]
# For demo - add 10 new mice to my population list
for i in range (10):
    population.append(createMouse("Black","White"))

# For demo, show how we can age the full population of mice by 1 month.
# For demo, do this 10 times
for i in range (20):
    ageOneMonth(population)
    print(population)


