import turtle, time, sys

sys.setrecursionlimit(10000005)
sys.set_int_max_str_digits(999999999)
WIDTH, HEIGHT = 1000, 1000 # set GUI screen size

def art_screen(): # func to initialize GUI
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Art')
    # turtle.color('black', 'pink')

def turtle_input():
    print('reading file for input...')
    with open('turtle_input.txt', 'r') as value_input:
        input_data = value_input.readlines()
    brush_data = ''.join(str(brush_data) for brush_data in input_data)
    brush_data = int(brush_data)
    return brush_data

def equation(x, y=0):
    if y == x:
        return x
    else:
        return (x * equation(x, y + 1)) ** x
    
def manual_input():
    mf_input = int(input('num input: '))
    print('calculating...')
    brush_data = equation(mf_input)
    return brush_data

def scribble(): # main func to run brush loop
    # brush_data = turtle_input()
    brush_data = manual_input()
    modifier = int(input('modifier: '))
    art_screen() # initialize GUI
    brush = turtle.Turtle() # initialize brush
    brush.left(90) # point brush upward
    for digit in str(brush_data): # brush loop
        print(digit) # debug
        digit = int(digit) # convert digit to int
        if digit % 2 == 0: # if even
            brush.right(digit * 10 * modifier) # turn brush
            print(f'right {digit * 10 * modifier} degrees') # debug
        else: # if odd
            brush.left(digit * 10 * modifier) # turn brush
            print(f'left {digit * 10 * modifier} degrees') # debug
        brush.forward(digit * modifier) # draw line
        print(f'paint {digit * modifier} pixels') # debug
    time.sleep(180) # GUI & script wait when finished

def draw(modifier=False, debug=False): # main func to run brush loop
    brush_data = manual_input()
    if modifier: modifier = int(input('modifier: '))
    else: modifier = 1
    art_screen() # initialize GUI
    brush = turtle.Turtle() # initialize brush
    brush.pen(speed=10)
    brush.hideturtle()
    brush.penup()
    brush.setpos(-400, 0)
    brush.pendown()
    brush.fillcolor('#808080')
    brush.begin_fill()
    for index, digit in enumerate(str(brush_data)): # brush loop
        if debug: print(f'---\n'
                        f'step {index + 1} with digit {digit}:') # debug
        digit = int(digit) # convert digit to int
        if digit % 2 == 0: # if even
            brush.right(90) # turn brush
            if debug: print(f'right 90 degrees') # debug
        else: # if odd
            brush.left(90) # turn brush
            if debug: print(f'left 90 degrees') # debug
        brush.forward(digit * modifier) # draw line
        if debug: print(f'paint {digit * modifier} pixels') # debug
    brush.end_fill()
    time.sleep(178000) # GUI & script wait when finished

draw(debug=True)
# scribble()
# art()