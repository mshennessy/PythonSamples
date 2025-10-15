# Set up a list of countries
countries=["Ireland","France","Spain"]
capitals=["Dublin","Paris","Madrid"]

score = 0

# Go through the list and process each country
for i in range(len(countries)):
    print("What is the capital of ",countries[i])
    answer = input("?")
    # Compare the answer given with correct answer
    if answer == capitals[i]:
        print("Correct")
        score+=1
    else:
        print("Incorrect")

print("You scored",score,"out of",len(countries))