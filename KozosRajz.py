#Veszprémi Zalán, Jelzőlámpa: szines körök
#Szalai Dávid, Jelzőlámpa: oszlopok

import turtle

#alap
turtle.bgcolor("lightblue")
turtle.speed(0)
turtle.goto(0, -250)

#oszlop

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


#korok
turtle.penup()
turtle.goto(25, 285)
turtle.pendown()

#piros
turtle.color("red")
turtle.begin_fill()
turtle.circle(35)
turtle.end_fill()

turtle.penup()
turtle.goto(25, 205)
turtle.pendown()

#sarga
turtle.color("yellow")
turtle.begin_fill()
turtle.circle(35)
turtle.end_fill()

#zold
turtle.penup()
turtle.goto(25, 130)
turtle.pendown()

turtle.color("green")
turtle.begin_fill()
turtle.circle(35)
turtle.end_fill()

turtle.done()
