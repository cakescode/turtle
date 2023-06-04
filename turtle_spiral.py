import turtle, time

WIDTH, HEIGHT = 1000, 1000 # set GUI screen size

def art_screen(): # func to initialize GUI
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Art')

def rough_double_spiral(modifier=False):
    if modifier: modifier = modifier
    else: modifier = 1
    art_screen() # initialize GUI
    brush = turtle.Turtle()
    brush.hideturtle()
    brush.speed(10)
    for i in range(92):
        brush.forward(1 * modifier)
        brush.right(45 - i)
    time.sleep(178000)

def smooth_spiral(modifier=False):
    size = 25
    if modifier: modifier = modifier
    else: modifier = 1
    art_screen() # initialize GUI
    brush = turtle.Turtle()
    brush.hideturtle()
    brush.speed(10)
    for i in range(10000):
        brush.pensize(size)
        brush.forward(1 * modifier)
        if i > 0 and i % 10 == 0:
            brush.right(i / 100)
            if i % 60 == 0 and size >= 1:
                size -= 1
    time.sleep(178000)

rough_double_spiral(10)
# smooth_spiral()