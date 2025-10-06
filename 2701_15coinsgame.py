# Computational Thinking
# Simulation of 15 coin game
# G Hennessy CUS

from random import randint

coinsLeft = 15

while coinsLeft >= 2:
    p1_take=randint(1,2) # a number between 1 and 2 inclusive
    coinsLeft -= p1_take
    print("I have taken",p1_take,"coins. There are",coinsLeft,"left")
    # If it is zero, computer wins.
    if coinsLeft == 0:
        print("I win")
        break     # Simplifies code, exit here out of loop
    # Now it is your turn. Input a number. Make sure it is less than or
    # equal to the number of coins left
    
    
    # If you get to zero, you win.
    if coinsLeft == 0:
        print("You win")

print("Game over")
    
    
