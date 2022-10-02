import pgzrun
from random import randint
WIDTH = 1500
HEIGHT = 1000
apple = Actor('applerszcut')

def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = randint(200, 1300)
    apple.y = randint(200, 800)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shot!")
        place_apple()
    else:
        print("You missed! L player")
        quit()

place_apple()
pgzrun.go()
