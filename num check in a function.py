def verifyNum(text,lower,upper):
    validInput=False
    numUnverified=input(text)
    while (not validInput):
        if(numUnverified.isnumeric()):
            #convert to integer
            numVerified = int(numUnverified)
        else:
            print("Must be numeric")
            #make the value invalid so it will be caught in next if stmt
            numVerified=0
        if(numVerified<lower or numVerified >upper):
            print("Invalid input")
            numUnverified=input(text)
        else:
            #Trigger an exit from my while loop
            validInput = True
    print("Thankyou!")
    return(numVerified)

#Now in main code, we can call this function as often as we need
dd=verifyNum("Enter day dd [1-31]: ",1,31)
mm=verifyNum("Enter month mm [1-12]: ",1,12)
yy=verifyNum("Enter year yyyy :",1930,2022)
print("We have a valid date", dd,"/",mm,"/",yy)
#Just to demo .. numbers can ba anything"
zz=verifyNum("Guess a number between 1 and 10",1,10)


   

