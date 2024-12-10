# cody matheney
#p4lab1
#10/29/2024

# import libary
import turtle

#set up the window
window = turtle.Screen()
tom = turtle.Turtle()

# change fetures of turtle
tom.pensize(10)
tom.pencolor("red")
tom.shape("arrow")

#while loop that runs 4 times
movement=0

while movement <=3:
    movement+=1
    tom.forward(150)
    tom.right(90)

# for loop to run 3 times
for side in range(3):
    tom.forward(150)
    tom.left(120)
    
