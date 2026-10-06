from turtle import *
speed(100)

shape("arrow")
#we want tu paint a house

#step 1:  draw a square
#speed(30)

width(7)

color("purple")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward (70)
color("yellow")
begin_fill()
left(90)
forward(120)     #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a left window
penup()
goto(25, 130)    #position left window above the door
setheading(0)   #reset turtle orientationstraight right
pendown()


color("green")
begin_fill()
for _ in range(4):
   forward(40)
   left(90)
end_fill()

#drawing a right door
penup()
goto(135, 130)    #position right window symmetrically
pendown()


color("green")
begin_fill()
for _ in range(4):
   forward(40)
   left(90)
end_fill()    #end of the house


hideturtle()
exitonclick()  