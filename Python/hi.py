import turtle as t
from PIL import Image

t.speed(0)
t.ht()
t.colormode(255)

im = Image.open(input('image : '))
image = []
for pixel in list(im.getdata()):
    image.append(pixel)

def sq(x,y,t,color='black',fill=False): #Draw a square with specific parameters
    if fill:
        t.begin_fill()
    
    t.color(color)
    for i in range(2):
        t.fd(x)
        t.left(90)
        t.fd(y)
        t.left(90)

    if fill:
        t.end_fill()

def grid(x,y,array):
    t.pu()
    for i in range(y):
        print(x)
        print(i)
        for j in range(x):
            print((i*y)+j)
            t.pd()
            print(j)
            sq(10,10,t,color=array[((i)*y)+j],fill=True)
            t.fd(11)
            t.pu()
        t.sety(t.ycor()-(11))
        t.setx(t.xcor()-((10*x)+x))

grid(20,20,image)

t.done()