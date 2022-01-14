# This problem displays a detailed background where three turtles, having been named by the user
# will race. Once the winner is displayed on the console, fireworks appear in the background. The winner 
# will then be displayed on a podium. 
# Note that, if the user names the turtles the same name, the program will ask for a different name
# until all turtles have different names. 

import turtle 
import random 

def creating_background():
 # set the background color 
 turtle.bgcolor("green") 
 turtle.pensize(3)
 turtle.color("black")
 turtle.speed(0)
 # set the black sky 
 turtle.penup() 
 turtle.setpos(-500,-200) # the position where the sky will be filled 
 turtle.pendown()
 turtle.color("black")
 turtle.begin_fill()
 
# set the grass 
 i = 0 
 while i < 3: # less than 3 because a rectangle has two sides 
    turtle.forward(1000) # the base 
    turtle.left(90)
    turtle.forward(700) #the height
    turtle.left(90) # makes a right angle when it turns left 
    i += 1 
 turtle.end_fill()
 # set the sun 
 turtle.penup()
 turtle.setposition(-370, 370)
 turtle.pendown()
 turtle.color("yellow")
 turtle.begin_fill() # this function tells turtle that the upcoming object
# needs to be filled by the chosen color 
 turtle.circle(40)
 turtle.end_fill()
# first tree - trunk 
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
 
# first tree - leafs 
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
# second tree - trunk 
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
 
# second tree - leafs 
 turtle.color("green", "green")
 turtle.penup()
 turtle.setpos(400,-200)
 turtle.right(200)
 turtle.forward(200)
 turtle.pendown()
 turtle.begin_fill()
 turtle.circle(90)
 turtle.end_fill()
 
# In order to make this game fair, it must be random, thus we import the random package 
# Create a dice similiar to a random dice game like "Beat that!"
def random_winner_generator(turtle_a, turtle_b, turtle_c):

 dice = [1,2,3]
 turtle_speed = 15 
 turtle.speed(100) # adjusting the turtle's speed 
 winner = ""
 for i in range(40):
    if  turtle_a.position() >= (400, 100):
        print("The winner is", name_1)
        winner += name_1
        break
    elif turtle_b.position() >= (400, -100):
        print("The winner is",name_2)
        winner += name_2
        break
    elif turtle_c.position() >= (400, 100):
        print("The winner is", name_3)
        winner += name_3
        break
    else:
        dice_roll = random.choice(dice) #it choses a random value from the dice list 
        turtle_a.forward(turtle_speed*dice_roll) #mutiply 15 by a random number from the dice which will make the turtle move forward
        dice_rollb = random.choice(dice) 
        turtle_b.forward(turtle_speed*dice_rollb)
        dice_rollc = random.choice(dice)
        turtle_c.forward(turtle_speed*dice_rollc)
        
 return winner 
     
def draw_fireworks():  
     
 diff_colors = ["red", "blue", "aqua", "orange", "violet", "pink"] 
 turtle.speed(0)
 turtle.penup()
 turtle.goto(-200,250)
 turtle.pendown()
 turtle.color(random.choice(diff_colors))
 for i in range(36):
    turtle.forward(100)
    turtle.backward(100)
    turtle.left(10)
 turtle.penup()
 turtle.goto(300,250)
 turtle.pendown()
 turtle.color(random.choice(diff_colors))
 for i in range(36):
    turtle.forward(100)
    turtle.backward(100)
    turtle.left(10)
 turtle.penup()
 turtle.goto(120,100)
 turtle.pendown() 
 turtle.color(random.choice(diff_colors))  
 for i in range(36):
    turtle.forward(100)
    turtle.backward(100)
    turtle.left(10) 

def winner_on_podium(n):
     
  turtle.penup()
  turtle.setpos(0,-200)
  turtle.left(110)
  turtle.pendown()
  turtle.color("pink")
  turtle.begin_fill()
  turtle.forward(70)
  turtle.right(90)
  turtle.forward(120)
  turtle.right(90)
  turtle.forward(70)
  turtle.right(90)
  turtle.forward(120)
  turtle.end_fill()
  
  if n == name_1:
      turtle_a.penup()   
      turtle_a.goto(-35,-55)
      turtle_a.pendown()
           
  elif n == name_2:
      turtle_b.penup()   
      turtle_b.goto(-35,-55)
      turtle_b.pendown()   
          
  else:
      turtle_c.penup()   
      turtle_c.goto(-35,-55)
      turtle_c.pendown()    
  turtle.penup()   
  turtle.goto(-250,-10)
  turtle.pendown()
  style = ('Courier', 20, 'italic')
  message = "The winner is " + n 
  turtle.write(message, font = style)
     
if __name__ == "__main__":
   name_1 = input("Enter a turtles name: ")
   name_2 = input("Enter a turtles name: ")
   name_3 = input("Enter a turtles name: ")

   while name_1 == name_2 or name_2 == name_3 or name_1 == name_3:
       new_name = input("Liar try again: ")
       if new_name != name_1 and new_name != name_2 and new_name != name_3:
         break
       
   turtle_a, turtle_b, turtle_c = str(name_1), str(name_2), str(name_3)
   
   creating_background()
   # turtle_a
   turtle_a = turtle.Turtle()
   turtle_a.color("red")
   turtle_a.shape("turtle")
   turtle_a.shapesize(2,2,0)
   turtle_a.penup()
   turtle_a.setpos(-400,-250)
   # turtle_b
   turtle_b = turtle_a.clone()
   turtle_b.color("blue")
   turtle_b.penup()
   turtle_b.setpos(-400,-300)
   
   # turtle_c
   turtle_c = turtle_a.clone()
   turtle_c.color("purple")
   turtle_c.penup()
   turtle_c.setpos(-400,-350)
   
   turtle_a.pendown()
   turtle_b.pendown()
   turtle_c.pendown()

   n = random_winner_generator(turtle_a, turtle_b, turtle_c)
   draw_fireworks()  
   winner_on_podium(n)
   turtle.done()
