import turtle

def draw_rectangle(some_turtle):
    for x in range(1,5):
        some_turtle.forward(50)
        if (x%2==1):
            some_turtle.right(60)
        else:
            some_turtle.right(120)


def draw_flower():
    window = turtle.Screen()
    window.bgcolor("black")
    
    flower = turtle.Turtle()
    flower.shape("circle")
    flower.color("red")
    flower.speed(1)

    for i in range(1,37):
        draw_rectangle(flower)
        flower.right(10)

    flower.color("green")
    flower.right(90)
    flower.forward(200)

    window.exitonclick()
    
draw_flower()   
    
