from itertools import combinations
from random import choices

import matplotlib.pyplot as plt



class SlotMachine:
    
    def __init__(self, credit=100):
        self.init_credit = credit
        self.credit = self.init_credit
        self.text("You have $%s" %self.credit, y=0.5)
    
    
    def text(self, s, y=0, size=35, **kwargs):
        plt.axis("off")
        
        return plt.text(0.5, y, s, size=size, horizontalalignment="center", **kwargs)
    
    
    def __iter__(self):
        self.credit = self.init_credit
        
        plt.cla()
        self.text("You have $%s" %self.credit, y=0.5)
        
        return self
    
    
    def __next__(self):
        
        while self.credit >= 10:
            choice = choices(["\u2654", "\u2655", "\u2656", "\u2657", "\u2658", "\u2659"], k=3)
            score = sum([c[0] == c[1] for c in combinations(choice, 2)])
            
            plt.cla()
            self.text(" ".join(choice), y=0.5, size=100)

            if score == 0:
                self.credit -= 10
                self.text("You have won $0\n", color="b", size=30)
                self.text("Now you have $%s" %self.credit)

            elif score == 1:
                self.credit -= 5
                self.text("You have won $5\n", color="g", size=30)
                self.text("Now you have $%s" %self.credit)

            elif score == 3:
                self.credit += 90
                self.text("Congratulation!!!", y=0.3, color="r", size=25)
                self.text("You have won $100\n", color="r", size=30)
                self.text("Now you have $%s" %self.credit)

            return self.credit
        raise StopIteration
    
    
    def restart(self):
        self.__iter__()
    
    
    def spin(self): 
        try:
            self.credit = self.__next__()

        except StopIteration:
            plt.cla()

            if self.credit > 0:
                self.text("You have only $%s!" %self.credit, y=0.5)
                self.text("GAME OVER!!!", y=0.2, color="r")

            else:
                self.text("You have lost all money!", y=0.5)
                self.text("GAME OVER!!!", y=0.2, color="r")
