import arcade
from random import randint
GRAVITY_CONSTANT = 750
NUM_BASE = 5
NUM_STAR = 1
BASE_MOVEMENT_CONSTANT = -4
STAR_MOVEMENT_CONSTANT = -10
BULLET_MOVEMENT_CONSTANT = 30
ASTEROID_MOVEMENT_CONSTANT = -3
HEART_MOVEMENT_CONSTANT = -2
NUM_ASTEROID = 1
NUM_HEART = 1
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

class Base(arcade.Sprite):
    def __init__(self,world,x,y):
        super().__init__('images/base_3.png')
        self.world = world
        self.center_x = x
        self.center_y = y
        self.change_y = BASE_MOVEMENT_CONSTANT

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

class YellowStar(arcade.Sprite):
    def __init__(self,world,x,y):
        super().__init__('images/star.png')
        self.world = world
        self.center_x = x
        self.center_y = y
        self.change_y = STAR_MOVEMENT_CONSTANT
    def update(self,delta):
        super().update()

class BlackStar(arcade.Sprite):
    def __init__(self,world,x,y):
        super().__init__('images/star3.png')
        self.world = world
        self.center_x = x
        self.center_y = y
        self.change_y = STAR_MOVEMENT_CONSTANT
    def update(self,delta):
        super().update()

class Bullet(arcade.Sprite):
    def __init__(self,world,x,y):
        super().__init__('images/bullet.png')
        self.world = world
        self.center_x = x
        self.center_y = y
        self.change_y = BULLET_MOVEMENT_CONSTANT
    def update(self,delta):
        super().update()
class Asteroid(arcade.Sprite):
    def __init__(self,world,x,y):
        super().__init__('images/asteroid.png')
        self.world = world
        self.center_x = x
        self.center_y = y
        self.change_y = ASTEROID_MOVEMENT_CONSTANT
    def update(self,delta):
        super().update()
class Heart(arcade.Sprite):
    def __init__(self,world,x,y):
        super().__init__('images/hud_heartFull.png')
        self.world = world
        self.center_x = x
        self.center_y = y
        self.change_y = HEART_MOVEMENT_CONSTANT
    def update(self,delta):
        super().update()

class World:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.alien = Alien(self, 400, 800)

        self.alien_list = arcade.SpriteList()
        self.alien_list.append(self.alien)

        self.base_list = arcade.SpriteList()
        self.yellowstar_list = arcade.SpriteList()
        self.blackstar_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()
        self.heart_list =  arcade.SpriteList()
        for x in range(NUM_BASE):
            self.base_list.append(Base(self, randint(100,700),200*(x+1)))
        self.checkstar = 0
        self.checkasteroid = 0
        self.checkheart = 0
    def update(self,delta):
        self.alien.update(delta)
        self.makestar = randint(0,1000)
        self.randomstar = randint(1,3)
        self.makeasteroid = randint (0,1750)
        self.makeheart = randint(0,7500)
        for x in range(NUM_ASTEROID):
            if self.makeasteroid < 20 and self.checkasteroid < 3:
                self.asteroid_list.append(Asteroid(self,randint(50,750),1000))
                self.checkasteroid += 1
        for x in range(NUM_STAR):
            if self.makestar < 20 and self.checkstar == 0 and self.randomstar < 3:
                self.yellowstar_list.append(YellowStar(self,randint(20,780),1000))
                self.checkstar = 1
            elif self.makestar < 20 and self.checkstar == 0 and self.randomstar == 3:
                self.blackstar_list.append(BlackStar(self,randint(20,780),1000))
                self.checkstar = 1 
        for x in range(NUM_HEART):
            if self.makeheart < 20 and self.checkheart == 0:
                self.heart_list.append(Heart(self,randint(20,750),1000))
                self.checkheart = 1
        for yellowstar in self.yellowstar_list:
            yellowstar.update(delta)
            if yellowstar.center_y < 0:
                yellowstar.kill()
                self.checkstar = 0
        for blackstar in self.blackstar_list:
            blackstar.update(delta)
            if blackstar.center_y < 0:
                blackstar.kill()
                self.checkstar = 0
        for asteroid in self.asteroid_list:
            asteroid.update(delta)
            if asteroid.center_y < 0:
                asteroid.kill()
                self.checkasteroid -= 1

        for base in self.base_list:
            base.update(delta)
        for heart in self.heart_list: 
            heart.update(delta)
            if heart.center_y < 0:
                heart.kill()
                self.checkheart = 0 
        
        
