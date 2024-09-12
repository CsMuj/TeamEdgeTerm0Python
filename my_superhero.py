import time
import random 

class Super: 
    def __init__(self, nickname, health, power):
        self.nickname = nickname
        self.health = health
        self.power = power
        self.factor = round(random.random(), 2)

    def __repr__(self):
        return self.health

    def attack(self):
        return self.power * self.factor 

    def defend(self, enemies):
        return self.health * self.factor - enemies.attack()
        
    def isalive(self):
        return self.health > 0 

coder = Super("Mujtaba", 100, 100)
bugs = Super("Type Error", 100, 100)

while coder.isalive() and bugs.isalive():
    coder.defend(bugs)
    print(bugs)
    time.sleep(3)
    
    bugs.defend(coder)
    time.sleep(3)

#There may be an error. Stopped due to the game event.