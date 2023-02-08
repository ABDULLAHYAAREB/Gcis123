import turtle

wn = turtle.Screen()
t = turtle.Turtle()
t.width(1)

t.penup()
t.goto(-300, -200)


def rectangle(x, y, length, width, color):
    t.goto(x, y)
    t.pendown()
    t.color('black', color)
    t.begin_fill()
    t.forward(length)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(width)
    t.end_fill()
    t.penup()
    return x * y


def circle(x, y, radius, color):
    t.goto(x, y)
    t.pendown()
    t.color('black', color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.penup()


def mirror(x, y, color):
    t.goto(x, y)
    t.pendown()
    t.color('black', color)
    t.begin_fill()
    t.left(135)
    t.forward(30)
    t.left(45)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.backward(20)
    t.right(90)
    t.forward(20)
    t.left(45)
    t.forward(30)
    t.end_fill()
    t.penup()


def area(x, y):
    return x * y


def car():
    t.setheading(0)
    rectangle(-300, -200, 300, 150, "light green")
    t.setheading(0)
    rectangle(-250, -180, 100, 30, "cornflower blue")
    t.setheading(0)
    circle(-230, -190, 10, 'black')
    t.setheading(0)
    circle(-180, -190, 10, 'black')
    t.setheading(0)
    mirror(-160, -150, "alice blue")
    t.setheading(0)
    return area(300, 150)


def height(length, radious):
    return length + radious


def person(x, y):
    t.setheading(0)
    t.goto(x, y)
    t.pendown()
    t.left(55)
    t.forward(50)
    t.right(55)
    t.forward(10)
    t.right(55)
    t.forward(50)
    t.setheading(0)
    t.penup()
    t.goto(x, y + 40)
    t.pendown()
    t.forward(70)
    t.left(120)
    t.forward(70)
    t.left(120)
    t.forward(70)
    t.penup()
    t.setheading(0)
    t.goto(x, y + 40 + 35)
    t.pendown()
    t.forward(20)
    t.penup()
    t.goto(x + 30, y + 40 + 35)
    t.setheading(0)
    t.pendown()
    t.forward(20)
    t.penup()
    circle(x + 20, y + 40 + 55, 30, "")
    t.penup()
    return height(40 + 55, 30 / 2)


def tree(x, y):
    t.setheading(0)
    t.goto(x, y)
    t.pendown()
    t.color('black', 'green')
    rectangle(x, y, 20, 300, "sienna")
    circle(x - 30, y + 300, 50, "green")
    t.penup()


height = person(100, -300)
tree(200, -300)
area = car()

print("The area of the car is," + str(area) + " square units.")
print("The height of the person is " + str(height / 100) + " mt.")

turtle.done()