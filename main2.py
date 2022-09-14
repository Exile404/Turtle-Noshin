from turtle import *

import turtle as tur
tur.speed(100)

def drawoval(rad):
    for x in range(2):
        tur.circle(rad, -90)
        tur.circle(rad // 2, -90)
def drawoval1(rad):
    for x in range(2):
        tur.circle(rad, 90)
        tur.circle(rad // 2, 90)
def drawoval2(rad):
def drawoval4(rad):
    for x in range(2):
        # tur.circle(rad, -90)
        tur.circle(rad // 2, -90)
def draw_rectangle5(board, x, y, width, height, size, color):
    board.pencolor(color)
    board.pensize(size)
    tur.fillcolor('#461d15')
    board.setheading(0)
    tur.begin_fill()
    board.up()
    board.goto(x, y)
    board.down()
    # draw top
    board.forward(width)
    # draw right
    board.right(90)
    board.forward(height)
    # draw bottom
    board.right(90)
    board.forward(width)
    # draw left
    board.right(90)
    board.forward(height)
    board.end_fill()


tur.seth(-45)
#To go to the desired postion


# Hair

tur.up()
tur.pencolor('#461d15')
tur.pensize(5)
tur.fillcolor('#461d15')
tur.begin_fill()
tur.goto(-150, 30)
tur.right(45)
tur.down()
drawoval4(350)
tur.end_fill()
tur.up()
draw_rectangle5(tur,-150,30,350,200,5,"#461d15")
tur.up()


tur.seth(-45)
#To go to the desired postion
tur.fillcolor("#f2cca0")

# face
tur.begin_fill()
tur.up()
tur.goto(-50, -200)
tur.down()
drawoval(200)
tur.end_fill()

#Right Eye
tur.up()
tur.goto(60, 10)
tur.fillcolor("white")
tur.pencolor("#f2cca0")
tur.begin_fill()
drawoval1(30)
tur.end_fill()
tur.left(70)
tur.fd(19)
tur.color("black")
tur.dot(20)
tur.end_fill()

#Left EYe

tur.up()
tur.right(70)
tur.goto(-60, 10)
tur.fillcolor("white")
tur.begin_fill()
drawoval1(30)
tur.end_fill()
tur.left(70)
tur.fd(19)
tur.color("black")
tur.dot(20)
tur.up()

#Mouth

tur.goto(-30, -130)
tur.down()
tur.right(90)
tur.circle(60, 130)
tur.up()


#Nose

tur.goto(50, -100)
tur.down()
tur.right(65)
tur.pensize(2)
tur.bk(15)
tur.up()
tur.bk(20)
tur.right(90)
tur.down()
tur.circle(10, 180)
tur.up()
tur.right(90)
tur.bk(20)
tur.down()
tur.bk(15)
tur.up()

#Right Ear

tur.goto(150, -30)
tur.pencolor("#f2cca0")
tur.dot(80)
tur.fd(10)
tur.pencolor("#ebdac7")
tur.dot(20)
tur.up()


#Left Ear

tur.goto(-110, -30)
tur.left(100)
tur.down()
tur.pencolor("#f2cca0")
tur.dot(80)
tur.fd(10)
tur.pencolor("#ebdac7")
tur.dot(20)
tur.up()


#Hair

# tur.pencolor("#461d15")
# tur.goto(10, 100)
# tur.right(100)
# tur.down()
# tur.left(120)
# tur.begin_fill()
# tur.fd(20)
# tur.left(120)
# tur.fd(20)
# tur.end_fill()
#
# tur.begin_fill()
# tur.right(120)
# tur.fd(40)
# tur.left(120)
# tur.fd(40)
# tur.end_fill()
# tur.up()
# tur.goto(100, 90)
# tur.right(60)
# tur.down()
# tur.pensize(20)
# tur.fd(150)
# tur.up()
# tur.goto(110, 107)
# tur.down()
# tur.fd(150)


#Birth sign

tur.up()
tur.goto(-40, 70)
tur.fillcolor("black")
tur.begin_fill()
tur.circle(5)
tur.end_fill()
tur.up()


#Right Spectacle


tur.goto(120, 0)
tur.right(55)
tur.pencolor("black")
tur.pensize(2)
tur.down()
#tur.seth(1)

drawoval(45)
#Left Spectacle
tur.up()
tur.goto(-70,35)
tur.right(180)
tur.pencolor("black")
tur.pensize(2)
tur.down()
#tur.seth(1)
drawoval(45)
tur.up()
draw_rectangle1(tur,50,20,45,40,2,"black")
tur.done()
