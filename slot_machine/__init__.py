import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations



def text(s, y=0, size=35, **kwargs):
        plt.axis("off")
        return plt.text(0.5, y, s, size=size, horizontalalignment="center", **kwargs)



def slot_machine(credit):
    text("You have $%s" %credit, y=0.5)
    yield credit
    
    while credit >= 10:
        choice = np.random.choice(["\u2654", "\u2655", "\u2656", "\u2657", "\u2658", "\u2659"], 3)
        plt.cla()
        text(" ".join(choice), y=0.5, size=100)
        score = sum([c[0] == c[1] for c in combinations(choice, 2)])
        
        if score == 0:
            credit -= 10
            text("You have won $0\n", color="b", size=30)
            text("Now you have $%s" %credit)
            
        elif score == 1:
            credit -= 5
            text("You have won $5\n", color="g", size=30)
            text("Now you have $%s" %credit)
            
        elif score == 3:
            credit += 90
            text("Congratulation!!!", y=0.3, color="r", size=25)
            text("You have won $100\n", color="r", size=30)
            text("Now you have $%s" %credit)
        
        yield credit



def game(credit=100):
    global game_gener
    game_gener = slot_machine(credit)



def spin():
    global credit
    
    try:
        credit = next(game_gener)
        
    except StopIteration:
        plt.cla()
        
        if credit > 0:
            text("You have only $%s!" %credit, y=0.5)
            text("GAME OVER!!!", y=0.2, color="r")
            
        else:
            text("You have lost all money!", y=0.5)
            text("GAME OVER!!!", y=0.2, color="r")



game()
