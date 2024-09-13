# G Hennessy CUS
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

# Initialise the grid as a 2-dimensional array (list of lists in python)
fullGrid =[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

#Print the entire grid
def printGrid(grid):
  # For each row of the grid
  for i in range(len(grid)):
    #For eachh element in the row
    for j in range(len(grid[i])):
      # print the element with a colour background green or red
      if grid[i][j] == 0:
        print(Back.GREEN, grid[i][j],end= '')
      else:
        print(Back.RED, grid[i][j],end= '')
    print()
 
printGrid(fullGrid)

# Now change elements of the grid in multiple passes over the whole grid
for i in range(len(fullGrid)):
  for j in range(len(fullGrid[i])):
    # change each element in the row to a 0 or 1
    fullGrid[i][j]=randint(0,1)
  # Pause for a second so that we can see the grid change
  sleep(1)
  # Clear the screen (NB this bit is Replit only)
  clear()
  # Print the entire grid with updates
  printGrid(fullGrid)
