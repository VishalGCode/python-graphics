import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set the background color

# Create a turtle object
star = turtle.Turtle()
star.shape("turtle")
star.speed(10)  # Set speed to fastest
star.width(2)

# List of colors for the star
colors = ["red", "yellow", "blue", "green", "purple", "orange", "cyan"]

# Draw a colorful star
for i in range(50):
    star.pencolor(colors[i % len(colors)])  # Cycle through the colors
    star.forward(i * 10)
    star.right(144)  # Turn the turtle right by 144 degrees

# Hide the turtle once finished
star.hideturtle()

# Keep the window open
turtle.done()
