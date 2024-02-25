from turtle import Turtle, Screen
#the program is written just for playing around with and exploring the Turtle GUI.
jack = Turtle()
jack.shape("turtle")
jack.width(10)
jack.color('red')
jack.fillcolor('yellow')
for steps in range(100):
  jack.forward(steps)
  jack.right(30)

while True:
    jack.forward(10)
    jack.left(45)
    if abs(jack.pos()) < 1:
        break
my_screen = Screen()
my_screen.exitonclick()