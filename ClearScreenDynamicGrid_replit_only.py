# G Hennessy CUS
# Demo of how to give a dynamic display on replit using the replit clear() function
# Note that this isn't available on Thonny, so the grids will just appear sequentially

# Import the clear() function
# Note that this won't work on Thonny even if you install replit module
from replit import clear
# Import the sleep function for a time delay so we can see the grid changing
from time import sleep
# Import random choice
from random import randint

fullGrid =[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

def printGrid(grid):
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      print(grid[i][j], end="")
    print()

for i in range(len(fullGrid)):
  for j in range(len(fullGrid[i])):
    # change each element in the row to a 0 or 1
    fullGrid[i][j]=randint(0,1)
  sleep(1)
  clear()
  printGrid(fullGrid)
