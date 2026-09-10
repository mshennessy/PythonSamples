# 4031 - Framework for a simulation
# G Hennessy CUS

# Your code should be broken down into functions (such as create_child(), pass_1_year() etc)
# You can keep the population list (children=[]) global so you can access it from anywhere in your code

import random
# This will be a list of all the "agents" in my simulation
# This will be a list of lists (where each sub-list = 1 child)
children=[]

# Each agent in the simulation is a child with an age, a nutrition level and a height
# Indices for child list made into words so that the code is easier to follow
# eg child[AGE] is the same as child[0]
child=[]
AGE=0
NUTRITION=1
HEIGHT=2
# So we could end up with for example 3 children in a list like this
# children =[[10,1,150],[14,3,162],[25,1,182]]
for i in range(5):       # Start with 5 people
    # Build the data for a single child
    age=random.randint(1,18)    # Assign a random age
    child.append(age)
    # Add a nutrition factor - a value between 1 and 3 for bad, average or good nutrition
    nutrition=random.randint(1,3)
    child.append(nutrition)
    # Formula (model) for a random height depending on age and nutrition with a random factor also
    # This took a bit of tweaking and could be improved on
    height=50+(age*(4+nutrition))+random.randint(-10,10)     #Create a new child
    child.append(height)
    # Add child to my list
    children.append(child)
    # Reinitialise child[]
    child=[]
 
print("Year one:")
for child in children:
    print ("Age:",child[AGE],"Height:",child[HEIGHT])
    
# Now simulate time passing - child[] gets older and taller
for i in range(5):
    # Simulate 1 year passing - adjust ages and heights
    for child in children:
        child[AGE]+=1     # Add a year
        if child[AGE]<21: # Assume no growth after 21
            child[HEIGHT]+=5
    print("Another year passes")
    for child in children:
        print ("Age:",child[AGE],"Height:",child[HEIGHT])