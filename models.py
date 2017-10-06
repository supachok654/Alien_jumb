import arcade
from random import randint
GRAVITY_CONSTANT = 750
NUM_BASE = 5

class Alien(arcade.Sprite):
    def __init__(self,world,x,y):
        super().__init__('images/alien1.png')
        self.world = world
        self.center_x = x
        self.center_y = y
        self.change_x = 0
        self.chnage_y = GRAVITY_CONSTANT

    def update(self,delta):
        super().update()
        if self.center_x > self.world.width:
            self.center_x = 0
        if self.center_x < 0:
            self.center_x = 800
        if self.center_y < 0:
            self.center_y = self.world.height

class Base(arcade.Sprite):
    def __init__(self,world,x,y):
        super().__init__('images/base_3.png')
        self.world = world
        self.center_x = x
        self.center_y = y
        self.change_y = -1

    def update(self,delta):
        super().update()
        if self.center_y > self.world.height:
            self.center_y = 0
        if self.center_y < 0:
            self.center_y = 1000
            self.center_x = randint(100,700)
        if self.center_x > self.world.width:
            self.center_x = 0
        if self.center_x < 0:
            self.center_x = 800

class World:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.alien = Alien(self, 400, 800)
        #self.base = Base(self,randint(100,700),randint(200,1000))
        self.base_list = arcade.SpriteList()
        for x in range(NUM_BASE):
            self.base_list.append(Base(self, randint(100,700),200*(x+1)))
        
    def update(self,delta):
        self.alien.update(delta)
        #self.base.update(delta)
        #self.base = Base(self,randint(100,700),randint(200,1000))
        #self.base_list.append(Base(self,randint(100,700),randint(200,1000)))
        for base in self.base_list:
            base.update(delta)

