import turtle
def batang_miring(x, y, lebar, tinggi, sudut):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(sudut)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(tinggi)
        turtle.right(90)
        turtle.forward(lebar)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

def logo_adidas():
    turtle.bgcolor("black")
    turtle.color("white")
    turtle.speed(0)
    
    batang_miring(100, -100, 20, 150, 135)  
    batang_miring(60, -100, 20, 100, 135)   
    batang_miring(20, -100, 20, 60, 135)   

    turtle.hideturtle()
    turtle.done()
turtle.penup()
turtle.goto(10, -160)
turtle.color("white")
turtle.write("adidas", font=("Arial", 24, "bold"))

logo_adidas()
