import pgzrun
import string
from random import choice, randint

WIDTH = 500
HEIGHT = 500
BLACK = (0,0,0)
WHITE = (255,255,255)
LETTER = dict()
LETTERS = list()

possible_score=0
for x in range(4):
    LETTER = {"letter":choice(string.ascii_letters).lower(),"x":randint(10, WIDTH -10),"y":0}
    LETTERS.append(LETTER)

LETTERS = [i for n,i in enumerate(LETTERS) if i not in LETTERS[n+1:]]
score = {"RIGHT":0,"WRONG":0}



VELOCITY = 1

def update():
    for i in range (4):
        LETTERS[i]["y"]+=VELOCITY
        if(LETTERS[i]["y"]==HEIGHT):
            score["WRONG"]+=1
            update_letter(i)
    # LETTER["y"]+=VELOCITY
    # if(LETTER["y"]==HEIGHT):
    #     LETTER["y"] = 0
    #     update_letter()

def update_letter(i):
    global LETTERS
    y = choice(string.ascii_letters).lower()
    if(LETTERS[i] != None):
        LETTERS[i] = {}
    for x in range (4):
        if y == LETTERS[x]["letter"] :
            update_letter(i)
    LETTERS[i]["letter"] = y
    LETTERS[i]["x"] = randint(10, WIDTH -10)
    LETTERS[i]["y"] = 0
   
    
def on_key_down(key, mod, unicode):
    if unicode:
        var = True
        for i in range(4):
            if LETTERS[i]["letter"] == unicode:
                var = False
                score["RIGHT"]+=1
                update_letter(i)
                # on_key_down(key,mod,unicode)
        if var:   
            score["WRONG"]+=1

            
        

def draw():
    screen.clear()
    screen.fill(BLACK)
    for i in range(4):
        COORDINATES = (LETTERS[i]["x"],LETTERS[i]["y"])
        screen.draw.text(LETTERS[i]["letter"],COORDINATES,color=WHITE,fontsize=30)
        screen.draw.text("RIGHT : " +str(score["RIGHT"]),(WIDTH-120,10),color = WHITE, fontsize = 20)
        screen.draw.text("WRONG : " +str(score["WRONG"]),(WIDTH-120,40),color = WHITE, fontsize = 20)


pgzrun.go()