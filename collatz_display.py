import turtle, time, sys

WIDTH, HEIGHT = 1000, 1000 # set GUI screen size

def art_screen(): # func to initialize GUI
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Collatz Conjecture Display')

REC_LIMIT = 10000
sys.setrecursionlimit(REC_LIMIT)

def collatz(x, step=0):
    if step > (REC_LIMIT - 7): # prevents error when stack is abt to overflow
        print(f'{x} exceeded recursion depth of {REC_LIMIT}')
        time.sleep(178000)
        exit()
    elif x == 1: # ends the recursion, returns the score (how many steps)
        return step
    elif x % 2 == 0: # if even, divide by 2
        return collatz(x // 2, step + 1)
    else: # if odd, multiply by 3 and add 1
        return collatz(3 * x + 1, step + 1)

def display_collatz(x=1):
    art_screen() # initialize GUI
    brush = turtle.Turtle() # initialize brush
    brush.hideturtle() # hide brush icon
    brush.speed(9999) # set brush to max speed
    brush.penup() # dont paint
    brush.left(90) # face brush upward
    while True: # loop collatz display infinitly
        brush.clear() # clear GUI
        most_steps = 0
        for i in range(975): # loop repeats till end of GUI, clears, repeats
            steps = collatz(x) # amt of times it takes for x to get to 1
            print(f' {x}: steps = {steps}  \t|  \ttallest line: '
                  f' {most_steps}') # relay data in terminal
            brush.setpos(-490 + i, -365) # position of line start
            brush.pendown() # paint
            brush.forward(steps) # line length is = to # of steps in pixels
            brush.penup() # dont paint
            x += 1 # go to next integer and repeat loop
            if steps > most_steps:
                most_steps = steps
            

display_collatz(1052936516)