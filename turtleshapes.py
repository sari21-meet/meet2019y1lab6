"""
import turtle

num_pts = 6 #number of sides to the drawing
for i in range(num_pts) :
    turtle.left(360/num_pts)
    turtle.forward(100)
turtle.mainloop()
"""
"""
result = []
n = 18
for count in range(1, n):
    if count % 3 == 0 and count % 5 == 0:
        result.append("fizzbuzz")


    elif count % 3 == 0:
        result.append("fizz")

    elif count % 5 == 0:
        result.append("buzz")
    
        
    else:
        result.append(count)

print(result)
"""
import turtle
turtle.tracer(1)
turtle.speed(500)
rounds = 10
size = 10
mike = turtle.clone()
steve = turtle.clone()
turtle.bgcolor("white")
turtle.hideturtle()
mike.color("gold")
steve.color("grey")
steve.goto(5,5)
while True:
    mike.circle(size)
    mike.left(180)
    steve.circle(-size)
    steve.left(-180)
    size += 10
turtle.mainloop()

