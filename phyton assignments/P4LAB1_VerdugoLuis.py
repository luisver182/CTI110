# Verdugo Luis
# 05/07/2025
# P4LAB1
# use of loops and turtle to draw

#import the library
import turtle

#create a turtle object
win = turtle.Screen()
pen = turtle.Turtle()

#set turtle option
pen.pensize(3)
pen.pencolor("turquoise")
pen.shape("turtle")

#code to draw the shapes
for side in range(4):
  pen.forward(100)
  pen.left(90)
#while loop that executes 3 times
sides=3
while sides > 0:
  pen.forward(100)
  pen.left(120)
  sides = sides - 1

win.mainloop()



