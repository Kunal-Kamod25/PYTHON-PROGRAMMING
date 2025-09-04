import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Happy Birthday Animation")

# Create turtle for balloons
balloon = turtle.Turtle()
balloon.hideturtle()
balloon.speed(0)

colors = ["red", "yellow", "blue", "green", "purple", "orange"]

def draw_balloon(x, y, color):
    balloon.penup()
    balloon.goto(x, y)
    balloon.pendown()
    balloon.color(color)
    balloon.begin_fill()
    balloon.circle(30)
    balloon.end_fill()
    # Draw string
    balloon.right(90)
    balloon.forward(60)
    balloon.left(90)
    balloon.penup()
    balloon.goto(x, y)
    balloon.pendown()

# Draw multiple balloons with animation
for i in range(6):
    x = -200 + i * 80
    y = random.randint(0, 100)
    draw_balloon(x, y, colors[i])
    time.sleep(0.5)

# Write Happy Birthday message with animation
writer = turtle.Turtle()
writer.hideturtle()

writer.penup()
writer.goto(-120, -50)
writer.color("magenta")
writer.pendown()
writer.write("Happy Birthday!", font=("Comic Sans MS", 32, "bold"))

# Keep the window open
turtle.done()