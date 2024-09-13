 G Hennessy CUS
# Demo of how to give a dynamic display on replit using the replit clear() function
# Note that this isn't available on Thonny, so the grids will just appear sequentially

# Import the clear() function
from replit import clear
# Import the sleep function for a time delay so we can see the grid changing
from time import sleep
# Import random choice
from random import randint
# Allow output to have a background colour
from colorama import Back

fullGrid =[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

def printGrid(grid):
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == 0:
        print(Back.GREEN, grid[i][j],end= '')
      else:
        print(Back.RED, grid[i][j],end= '')
    print()
    
printGrid(fullGrid)
for i in range(len(fullGrid)):
  for j in range(len(fullGrid[i])):
    # change each element in the row to a 0 or 1
    fullGrid[i][j]=randint(0,1)
  sleep(1)
  clear()
  # Print the entire grid with updates
  printGrid(fullGrid)
