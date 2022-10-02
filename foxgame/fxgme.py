import pgzrun
from random import randint

WIDTH = 1500
HEIGHT = 1000
score = 0
gmo = False 

fox = Actor("foxcut") 
fox.pos = 750, 500
coin = Actor("coincut")
coin.pos = 300, 300 

def draw():
    screen.fill("green")
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color = "black", topleft=(10,10))
    if gmo == True : 
        screen.fill("pink")
        screen.draw.text("Final score: " + str(score), color = "black", topleft=(10,10), fontsize = 60)


def place_coin():
    coin.x = randint(100, (WIDTH - 100))
    coin.y = randint(100, (HEIGHT - 100))

def time_up():
    global gmo
    gmo = True

def update():
    global score

    if keyboard.left:
        fox.x = fox.x-2
    if keyboard.right:
        fox.x = fox.x+2
    if keyboard.up:
        fox.y = fox.y-2
    if keyboard.down:
        fox.y = fox.y+2


    coin_collected = fox.colliderect(coin)

    if coin_collected:
        score = score + 10
        place_coin()


clock.schedule(time_up, 15.0)
pgzrun.go()

