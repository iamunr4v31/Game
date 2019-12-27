import pgzrun
import random


WIDTH = 500
HEIGHT = 500
TITLE = 'flappy-bird'


GRAVITY = 0.2
GAP = 130
FLAP_STR = 6.5
SPEED = 3


bird = Actor('flappy',(75,200))
bird.dead = False
bird.score = 0
bird.vy = 0
storage = {}

storage.setdefault('highscore',0)

def reset_pipes():
    pipe_gap_y = random.randint(200, HEIGHT-200)
    pipe_top.pos = (WIDTH, pipe_gap_y - GAP//2)
    pipe_bottom.pos = (WIDTH, pipe_gap_y + GAP//2)


pipe_top = Actor('top', anchor=('left','bottom'))
pipe_bottom = Actor('bottom', anchor=('left','top'))
reset_pipes()

def update_pipes():
    pipe_top.left -= SPEED
    pipe_bottom.left -= SPEED
    if pipe_top.right < 0:
        reset_pipes()
        if not bird.dead:
            bird.score+=1
            if bird.score > storage['highscore']:
                storage['highscore'] = bird.score


def update_bird():
    uy = bird.vy
    bird.vy +=GRAVITY
    bird.y += (bird.vy + uy) / 2

    if not bird.dead:
        if bird.vy < -3:
            bird.image = 'flappy1'
        else:
            bird.image = 'flappy2'

    if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom):
        bird.dead = True
        bird.image = 'dead'
    
    if not 0 < bird.y < 720:
        bird.y = 200
        bird.dead = False
        bird.score = 0
        bird.vy = 0
        reset_pipes()
    

def update():
    update_pipes()
    update_bird()


def on_key_down():
    if not bird.dead:
        bird.vy -= FLAP_STR


def draw():
    screen.blit('bgk', (0, 0))
    pipe_top.draw()
    pipe_bottom.draw()
    bird.draw()
    screen.draw.text(
        str(bird.score),
        color='white',
        midtop=(WIDTH // 2, 10),
        fontsize=70,
        shadow=(1, 1)
    )
    screen.draw.text(
        "Best: {}".format(storage['highscore']),
        color=(200, 170, 0),
        midbottom=(WIDTH // 2, HEIGHT - 10),
        fontsize=30,
        shadow=(1, 1)
    )


pgzrun.go()
