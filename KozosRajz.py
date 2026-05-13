#Veszprémi Zalán, 1. csoport, Jelzőlámpa
#Szalai Dávid, Jelzőlámpa

import turtle

#Alapbeallitas
turtle.speed(0)
turtle.pensize(3)
turtle.bgcolor("lightblue")
turtle.goto(0, -250)

#Oszlop
turtle.color("gray")
turtle.begin_fill()

i=0

while i<2 :
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(90)

    i+=1

turtle.end_fill()

turtle.left(90)
turtle.forward(300)
turtle.left(90)

#Láma Alap
turtle.color("black")
turtle.begin_fill()

turtle.forward(50)

turtle.right(90)
turtle.forward(250)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(250)

turtle.right(90)
turtle.forward(50)

turtle.end_fill()

turtle.done()
