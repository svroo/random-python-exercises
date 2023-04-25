from turtle import Screen, Turtle

def koch(tortuga, longitud, nivel):
    if nivel == 0:
        tortuga.forward(longitud)
    else:
        koch(tortuga, longitud/3, nivel-1)
        tortuga.left(60)
        koch(tortuga, longitud/3, nivel-1)
        tortuga.right(120)
        koch(tortuga, longitd/3, nivel-1)
        tortuga.left(60)
        koch(tortuga, longitud/3, nivel-1)

def copo(tortuga, longitud, nivel):
    koch(tortuga, longitud, nivel)
    tortuga.right(120)
    koch(tortuga, longitud, nivel)
    tortuga.rigth(120)
    koch(tortuga, longitud, nivel)

pantalla = Screen()
pantalla.setup(500, 500)
pantalla.screensize(500, 500)
pantalla.setworldcoordinates(0, -350, 500, 150) 
tortuga = Turtle()
tortuga.speed(9)
copo(tortuga, 400, 3)
pantalla.exitonclick()