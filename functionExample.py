# demo to show how functions and lists can streamline code

# Function to list out the options and get a selection from user
def offerChoice(options):
    validChoice=False
    while not validChoice:
        print("Your choices are")
        for i in options:
            print(" - ", i)
        choice=input("Choose:")
        if choice in options:
            # reset boolean value to exit while loop
            validChoice=True
    # return the user's choice
    return choice
    

# Define 3 lists of items
opt1=["asdsd","dfd","sds"]
opt2=["ahghhgfg","dftyuty","bcvbsds"]
opt3=["adfgsd","45trg","bhyyjy","sddf"]

# Start the user with 2 items
items=["sword","phone"]

# Append the users choice to the list of items 3 times.
items.append(offerChoice(opt1))
items.append(offerChoice(opt2))
items.append(offerChoice(opt3))

print("Your items :", items)