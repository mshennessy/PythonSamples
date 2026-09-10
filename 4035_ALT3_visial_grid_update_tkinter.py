# 4035 - simulation using visuals tkinter
# G. Hennessy CUS
# Demo code for a 5x5 grid with cells that change value
# as the code iterates

import tkinter  # You don't need to add this library

# Create the window
window = tkinter.Tk()
window.title("5 x 5 Array")  # Array is another name for "list"

# The array is actually a list of lists
# This array is initialised with values. It could be all zeroes
# and you write a function to populate it with random values
array = [
    [0, 1, 0, 2, 0],
    [1, 1, 0, 0, 2],
    [0, 0, 2, 3, 1],
    [2, 1, 1, 0, 0],
    [0, 2, 0, 1, 2]
]

# Draw the array
def draw_array():
    for row in range(5):
        for column in range(5):
            # This is how you reference a "cell" in your array
            # It works like x,y coordinates (or i,j vectors)
            if array[row][column] == 0:
                colour = "white"
            elif array[row][column] == 1:
                colour = "yellow"
            elif array[row][column] == 2:
                colour = "orange"
            elif array[row][column] == 3:
                colour = "red"
            elif array[row][column] == 4:
                colour = "brown"
            else:
                colour = "black"
            
            square = tkinter.Label(
                window,
                width=5,
                height=2,
                bg=colour,
                relief="solid"
            )
            
            square.grid(row=row, column=column)

def change_array(count):
    # Notice that count is 0 first time this function is called and
    # is incremented each time.
    # Then the .after() method calls this function again with the new
    # value for count. This is basically recursion, but asynchronous
    # recursion, handled by the tkinter library
    for row in range(5):
        for column in range(5):
            if array[row][column] <5:
                array[row][column] +=1
            
    print("Array:",array)
    draw_array()
    if count < 5:  # Just 5 iterations for demo
        window.after(1000, change_array, count + 1)

# Draw the first version of the array
draw_array()
# Now start off the updates. The last parameter 0 is to control the
# number of iterations. It's important not to just put this in a for or
# while loop as the python code will execute before the tkinter stuff.
# You'll just get the final version after all the updates instead of
# the dynamic updates.
# after() is a little unintuitive at first, but once you see it as
# “schedule the next step, then let mainloop() handle it”, it's much easier.
window.after(1000, change_array,0)

# Keep the window open - must be last
window.mainloop()