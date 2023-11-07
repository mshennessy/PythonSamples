import random
# get user details
firstName= input("Enter your firstname")
surName= input("Enter your surname")
year= input("Enter your year of birth YYYY")
#Build username according to rules
userName = surName[0:3] + '_' + firstName[0] + '_' + year[-2:]
print("Username is ", userName)

# Build a random password
number = random.randint(100,999)
symbol = random.choice(['@','%','£','/','$'])
letter = random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
passWord = letter + symbol + str(number)
print("Password is ", passWord)