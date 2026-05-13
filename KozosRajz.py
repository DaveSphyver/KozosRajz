#Veszprémi Zalán, Jelzőlámpa
#Szalai Dávid, Jelzőlámpa

import turtle

#alap
turtle.bgcolor("lightblue")
turtle.speed(0)

#korok
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()

#piros
turtle.color("red")
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 80)
turtle.pendown()

#sarga
turtle.color("yellow")
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

#zold
turtle.penup()
turtle.goto(0, -40)
turtle.pendown()

turtle.color("green")
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

turtle.done()
