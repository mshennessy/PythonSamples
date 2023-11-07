
# Step 1: Make all the "turtle" commands available to us.
import turtle



# Step 2: Create a new turtle. It will be called "pen"
pen = turtle.Turtle()
pen.goto(-300,0)  # now I can say pen.goto() instead of turtle.goto()
pen.speed(50)
pen.pencolor("red")
pen.pensize(20)
for i in range(20):
  pen.forward(200)
  pen.left(150)

pen.penup()
# Step 3 big shout
pen.goto(0,-400)
pen.color("red")
pen.pendown()
pen.write("CUS Red Army!",True, align="center", font=("Arial", 60, "normal"))
# Step 4: We're done!
turtle.done()

