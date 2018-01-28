from turtle import *
import time
import numpy as np

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
    turt=np.empty(6,object)
    pos=np.empty(6,object)
    for i in range(6):
        turt[i]=Turtle()
        turt[i].speed(4)
        turt[i].color([float(x) for x in np.random.rand(3)])
        turt[i].shape('turtle')
        turt[i].penup()
        turt[i].goto(0,-20-40*i)
        pos[i]=turt[i].position()
        turt[i].pendown()
    progress=np.zeros(6)    
    #for turn in range(100):
    while True:
        for i in range(6):
            val=np.random.randint(1,5)
            turt[i].forward(val)
            progress[i]+=val
            #print(i,'--',turt[i].position(),' VS ',pos[i])
            if turt[i].position()<=pos[i]:
                time.sleep(3)
                exit()
            elif progress[i]>=280:
                progress[i]=0
                turt[i].right(180)
        #print('')

if __name__ == '__main__':
    main()