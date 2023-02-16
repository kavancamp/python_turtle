import turtle

# --Functions--

# This is a square
keen_turtle = turtle.Turtle()
keen_turtle.speed(15)


def square():
  keen_turtle.forward(100)
  keen_turtle.right(90)
  keen_turtle.forward(100)
  keen_turtle.right(90)
  keen_turtle.forward(100)
  keen_turtle.right(90)
  keen_turtle.forward(100)

square()
keen_turtle.forward(200)
square()

elephant_weight = 3000
ant_weight = 0.1

#While Loop
if elephant_weight > ant_weight:
  square()
else:
  keen_turtle.forward(100)

  keen = 'happy'
  while keen == 'sad':
    keen_turtle.forward(10)

#For Loop

for i in range(10):
  print(i)

for count in range(3):
 square()


# This is a circle
# Initializing the turtle
k = turtle.Turtle()

# Radius for smallest circle
r = 10

# Number of circles
n = 8

# Loop for printing tangent circles
for i in range(1, n + 1, 1):
  k.circle(r * i)