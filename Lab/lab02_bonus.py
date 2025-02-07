import turtle as t

# Untuk menggambar angka 4
t.penup()
t.goto(-50,0)
t.pendown()
t.setheading(90)
t.back(50)
t.forward(100)
t.back(50)
t.setheading(180)
t.forward(50)
t.setheading(90)
t.forward(50)

#untuk menggambar angka 0
t.penup()
t.goto(-25,0)
t.pendown()
t.setheading(90)
t.back(50)
t.forward(100)
t.setheading(0)
t.forward(50)
t.setheading(-90)
t.forward(100)
t.setheading(180)
t.forward(50)

#untuk menggambar angka 4 lagi
t.penup()
t.goto(100,0)
t.pendown()
t.setheading(90)
t.back(50)
t.forward(100)
t.back(50)
t.setheading(180)
t.forward(50)
t.setheading(90)
t.forward(50)

t.exitonclick()