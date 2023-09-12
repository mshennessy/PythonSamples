# Model my CAO points outcome
from random import randint

#Function to calculate percentage score
def calculateGrade(innateSkill,work):
    if innateSkill == 'H':
        skillPoints = randint(70,100)
    elif innateSkill == 'M':
        skillPoints = randint(50,70)
    else:
        skillPoints = randint(0,50)
    # Calculate independant luck element luck is a value from 1-10
    
    luck = (randint(1,10)/10)
    print(luck)
    if work == 'H':
        workPoints = randint(70,100)
    elif work == 'M':
        workPoints = randint(50,70)
    else:
        workPoints = randint(0,50)
        
    subjGrade = (skillPoints + workPoints)/2
    #Factor in luck element
    #Calculate luck as a % of the missing marks
    #Eg I get 70%, so my luck-bonus is a % of 30
    bonus = (100 - subjGrade)*luck
    subjGrade += bonus
    return (subjGrade)

#Main code
print("welcome to your points simulator")
innateAbility = input("Enter your innate ability High/Medium/Low H/M/L")
workRate = input("Enter your work rate High/Medium/Low H/M/L")
#Call the function inside the print statement
print("Your percent calculated will be ", calculateGrade(innateAbility,workRate))


# How could this code be further developed?
# Put lines 33-36 in a loop asking for info about 7 LC subjects
# Add each result "Maths,H,H,88.4%", "German,L,M,58%" to a list and print results
# Write the list data to a CSV file
# Read it from a CSV file and print an output chart (eg scatter plot)
# Importantly, run the code many times (multiple simulations) and then see
# if it matches real-world outcomes. This would validate your model