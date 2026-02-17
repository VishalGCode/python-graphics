import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set background color of the screen

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Set turtle speed to the fastest
t.width(2)  # Set the pen width

# List of colors for the spiral
colors = ["red", "yellow", "blue", "green", "purple", "orange", "cyan"]

# Draw the spiral
for i in range(360):
    t.pencolor(colors[i % len(colors)])  # Cycle through colors
    t.forward(i * 3 / 2 + i)  # Move the turtle forward
    t.left(59)  # Turn the turtle left by 59 degrees

# Hide the turtle once finished
t.hideturtle()

# Keep the window open
turtle.done()
