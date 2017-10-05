import arcade
GRAVITY_CONSTANT = 750
class Alien:
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
        self.delta_x = 0
        self.delta_y = GRAVITY_CONSTANT
    def update(self,delta):
        if self.x > self.world.width:
            self.x = 0
        if self.x < 0:
            self.x = 800
        if self.y < 0:
            self.y = self.world.height
class Base:
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
    def update(self,delta):
        if self.y > self.world.height:
            self.y = 0
        if self.y < 0:
            self.y = 1000
        if self.x > self.world.width:
            self.x = 0
        if self.x < 0:
            self.x = 800
class World:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.alien = Alien(self,400,800)
        self.base = Base(self,400,200)
    def update(self,delta):
        self.alien.update(delta)
        self.base.update(delta)

