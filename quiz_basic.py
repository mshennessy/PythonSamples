#Basic code
#Add more countries/capitals
#Give >1 attempt per question
#Give a final score

countries=["Ireland", "Germany"]
capitals=["Dublin","Berlin"]

for i in range(len(countries)):
    print("What is the capital of",countries[i])
    ansCap= input("?")
    if (ansCap == capitals[i]):
        print("Correct")
    else:
        print("Wrong")
    print("next question")
print("This quiz is over")
        
        
        
        
        
        