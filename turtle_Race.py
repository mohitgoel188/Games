from turtle import *
import time
from random import randint

def main():
    speed(6)
    for step in range(15):
        write(step,align='center')
        penup()
        right(90)
        forward(10)
        pendown()
        forward(220)
        penup()
        backward(230)
        left(90)
        forward(20)
    ada=Turtle()
    ada.color('blue')
    ada.shape('turtle')
    ada.penup()
    ada.goto(0,-20)
    ada.pendown()
    rada=Turtle()
    rada.color('red')
    rada.shape('turtle')
    rada.penup()
    rada.goto(0,-60)
    rada.pendown()
    bada=Turtle()
    bada.color('black')
    bada.shape('turtle')
    bada.penup()
    bada.goto(0,-100)
    bada.pendown()
    yada=Turtle()
    yada.color('yellow')
    yada.shape('turtle')
    yada.penup()
    yada.goto(0,-140)
    yada.pendown()
    gada=Turtle()
    gada.color('green')
    gada.shape('turtle')
    gada.penup()
    gada.goto(0,-180)
    gada.pendown()
    brada=Turtle()
    brada.color('brown')
    brada.shape('turtle')
    brada.penup()
    brada.goto(0,-220)
    brada.pendown()
    for turn in range(100):
        ada.forward(randint(1,5))
        bada.forward(randint(1,5))
        rada.forward(randint(1,5))
        yada.forward(randint(1,5))
        gada.forward(randint(1,5))
        brada.forward(randint(1,5))
    time.sleep(3)
if __name__ == '__main__':
    main()