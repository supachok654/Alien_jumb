import arcade

class Alien:
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
    def update(self,delta):
        if self.x > self.world.width:
            self.x = 0
        if self.x < 0:
            self.x = 800
class World:
    def __init__(self,width,height):
        self.width = width
        self.height = height

        self.alien = Alien(self,400,800)
    def update(self,delta):
        self.alien.update(delta)        