# This problem displays a detailed background where three turtles, having been named by the user
# will race.The winner will be printed on the console and 
# once the winner is announced, fireworks are displayed in the background. However, if the user
# names the turtles the same name, the program will ask for a different name until all turtles have different names. 

import turtle 
import random 

turtle_a = input("Enter a turtles name: ")
turtle_b = input("Enter a turtles name: ")
turtle_c = input("Enter a turtles name: ")


while turtle_a == turtle_b or turtle_b == turtle_c or turtle_a == turtle_c:
     foundNewName = False 
     new_turtle = input("Liar try again:  ")
     if new_turtle != turtle_a and new_turtle != turtle_b and new_turtle != turtle_c:
         foundNewName = True
     if foundNewName == True:
      break 

        
new_winner1 = str(turtle_a)
new_winner2 = str(turtle_b)
new_winner3 = str(turtle_c)


# set the background color and pen size 
turtle.bgcolor("green") 
turtle.pensize(3)
turtle.color("black")
turtle.speed(0)

# This code will implement a black sky where it will take up most of the screen
 
turtle.penup() # we lift the penup to avoid dragging a line to our next position 
turtle.setpos(-500,-200) # the position where the sky is filled with blue
turtle.pendown()
turtle.color("black")
turtle.begin_fill()

# we need to code the grass where our 3 turtles will race which will 
# be a rectangle 
i = 0 # initialize a variable counter 
while i < 3: # less than 3 because a rectangle has two sides 
    turtle.forward(1000) # the base 
    turtle.left(90)
    turtle.forward(700) #the height
    turtle.left(90) # makes a right angle when it turns left 
    i += 1 # update our counter 
    
turtle.end_fill()


    
turtle.penup()
turtle.setposition(-370, 370) # go to this position on the screen
turtle.pendown()
turtle.color("yellow")
turtle.begin_fill() # this function tells turtle that the upcoming object
# needs to be filled by the chosen color 
turtle.circle(40)
turtle.end_fill()

# drawing the rectangle - base of the tree 
turtle.penup()
turtle.setpos(-350,-200)
turtle.pendown()
turtle.color("brown") # color of the trunk 
turtle.begin_fill()
turtle.forward(30) # width of the trunk 
turtle.right(90) # makes a right at a 90 angle 
turtle.forward(200) # the height of the trunk 
turtle.right(90)
turtle.forward(30) 
turtle.right(90)
turtle.forward(200)
turtle.end_fill()


# drawing the leafs- the body of my tree 
turtle.color("green", "green")
turtle.penup()
turtle.setpos(-350,-200) # go to this position 
turtle.right(200)
turtle.forward(200)
turtle.pendown()
turtle.begin_fill()
turtle.circle(90)
turtle.end_fill()

turtle.penup()
turtle.forward(150)
turtle.pendown()

# defining the second tree - drawing the trunk 
turtle.penup()
turtle.setpos(400,-200)
turtle.left(110)
turtle.pendown()
turtle.color("brown")
turtle.begin_fill()
turtle.forward(30)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(200)
turtle.end_fill()

# defining the second tree - drawing the leafs 
turtle.color("green", "green")
turtle.penup()
turtle.setpos(400,-200)
turtle.right(200)
turtle.forward(200)
turtle.pendown()
turtle.begin_fill()
turtle.circle(90)
turtle.end_fill()

       
# Now, define the three turltes, by initializing their shape, location, size and color 
    
# defining my first turtle, 
turtle_a = turtle.Turtle()
turtle_a.color("red")
turtle_a.shape("turtle")
turtle_a.shapesize(2,2,0)
turtle_a.penup()
turtle_a.setpos(-400,-250)
turtle_a.pendown()
    
# defining my second turtle 
turtle_b = turtle.Turtle()
turtle_b.color("blue")
turtle_b.shape("turtle")
turtle_b.shapesize(2,2,0)
turtle_b.penup()
turtle_b.setpos(-400,-300)
turtle_b.pendown()    
    
# defining my third turtle 
turtle_c = turtle.Turtle()
turtle_c.color("purple")
turtle_c.shape("turtle")
turtle_c.shapesize(2,2,0)
turtle_c.penup()
turtle_c.setpos(-400,-350)
turtle_c.pendown()
    
# make all turtles have their pen down 
turtle_a.pendown()
turtle_b.pendown()
turtle_c.pendown()


# In order to make this game fair, it must be random, thus we import the random package 
# Create a dice similiar to a random dice game like "Beat that!"
dice = [1,2,3]
turtle_speed = 15 
 
while i < 15:
    if  turtle_a.position() >=(400, 100):
        print("The winner is", new_winner1)
        break
    elif turtle_b.position() >= (400, -100):
        print("The winner is", new_winner2)
        break
    elif  turtle_c.position() >= (400, 100):
        print("The winner is", new_winner3)
        break
    else:
        dice_roll = random.choice(dice) #it choses a random value from the dice list 
        turtle_a.forward(turtle_speed*dice_roll) #mutiply 15 by a random number from the dice which will make the turtle move forward
        dice_rollb = random.choice(dice) 
        turtle_b.forward(turtle_speed*dice_rollb)
        dice_rollc = random.choice(dice)
        turtle_c.forward(turtle_speed*dice_rollc)
     
   
 
turtle.speed(100)

# initialize the colors of the fireworks 
diff_colors = ["red", "blue", "aqua", "orange", "violet", "pink"]

#define the function that will execute the fireworks which contain random colors from the above list 
def draw_fireworks():
 
 turtle.penup()
 turtle.goto(-200,250)
 turtle.pendown()

 turtle.color(random.choice(diff_colors))

 for i in range(36):
    turtle.forward(100)
    turtle.backward(100)
    turtle.left(10)
    
 turtle.penup()
 turtle.goto(0,0)
 turtle.pendown()
    
 turtle.penup()
 turtle.goto(300,250)
 turtle.pendown()
 
 turtle.color(random.choice(diff_colors))
    
 for i in range(36):
    turtle.forward(100)
    turtle.backward(100)
    turtle.left(10) 

 turtle.penup()
 turtle.goto(0,0)
 turtle.pendown()
 
 turtle.penup()
 turtle.goto(120,100)
 turtle.pendown()
 
 turtle.color(random.choice(diff_colors))
    
 for i in range(36):
    turtle.forward(100)
    turtle.backward(100)
    turtle.left(10) 
 

  
draw_fireworks()


turtle.done()
