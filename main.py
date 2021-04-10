from turtle import Turtle, Screen
import turtle
import random

timmy = Turtle()
#changing the shape 
# timmy.shape("turtle")

#Drawing a square
# timmy.color("Red")
# for _ in range(4):
#   timmy.forward(100)
#   timmy.left(90)

#Drawing a Dashed Line using turtle
# for _ in range(15):
#   timmy.forward(50)
#   timmy.penup()
#   timmy.forward(50)
#   timmy.pendown()

# timmy.color("Red")
# for _ in range(4):
#   timmy.forward(100)
#   timmy.right(90)
  
# timmy.color("yellow")
# for _ in range(5):
#   timmy.forward(100)
#   timmy.right(72)

# timmy.color("green")
# for _ in range(6):
#   timmy.forward(100)
#   timmy.right(60)


# timmy.color("purple")
# for _ in range(7):
#   timmy.forward(100)
#   timmy.right(360//7)


# timmy.color("pink")
# for _ in range(8):
#   timmy.forward(100)
#   timmy.right(360//8)

# timmy.color("brown")
# for _ in range(9):
#   timmy.forward(100)
#   timmy.right(360//9)

# timmy.color("orange")
# for _ in range(10):
#   timmy.forward(100)
#   timmy.right(360//10)

#colors list 
colors = ["CornflowerBlue" , "DarkOrchid", "IndianRed" , "DeepSkyBlue" , "wheat" ,"LightSeaGreen" ,"SlateGray", "SeaGreen"]

#drawing different shapes using for loop
# for i in range(3 , 11):
#   timmy.color(random.choice(colors))
#   for _ in range(i):
#     timmy.forward(100)
#     timmy.right(360 // i)

#Random Walk

turtle.colormode(255)

def random_colors():
  r = random.randint(0 , 255)
  g = random.randint(0 , 255)
  b = random.randint(0 , 255)
  return (r ,g , b)




#changing the speed of the turtle
timmy.speed("fastest") # it can be slow, fast , fastest , normal , slowest

#changing the pen size 
timmy.pensize(15) # giving the width of the pen


directions = [0, 90, 180 , 270]

for _ in range(300):
  timmy.color(random_colors())
  timmy.forward(20)
  timmy.setheading(random.choice(directions))


