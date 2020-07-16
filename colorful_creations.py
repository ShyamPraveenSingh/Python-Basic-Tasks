#Program to use colors in the python script

#use the turtle module
from turtle import *


#get an external screen of the specified size and color
screen = Screen()
screen.setup(1300, 1000)
screen.bgcolor('yellow')


#write text over it
color('black')
style = ('Times', 100, 'bold')
write('Shyam Praveen Singh', font=style, align='center')
hideturtle()

