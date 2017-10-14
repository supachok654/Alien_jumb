import arcade
import arcade.key
from models import World,Alien,Base,YellowStar,BlackStar
from random import randint
 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000
#GRAVITY_CONSTANT = 750 #เดี๋ยวมาแก้ ความโน้มถ่วงให้เพิ่มตามเวลาที่เปลี่ยนไป 
                       #โดยสร้างตัวแปรเวลามาเก็บ
                       #แล้วมาคูนกับ gravity
MOVEMENT_CONSTANT = 7
#BASE_CONSTANT_Y = 500
#BASE_CONSTANT_X = 500
#BOUNCINESS = 5
JUMP_CONSTANT = 20
FALL_CONSTANT = -10
CHANGE_Y_CONSTANT = 0.75
class AlienWindow(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width, height,"Alien Jump")
        self.background = None
        self.base_list = None
        self.yellowstar_list = None 
        self.blackstar_list = None
        self.world = World(width,height) 
        #self.alien_sprite = arcade.Spcd rite('images/alien1.png')
        #self.base_sprite = arcade.Sprite('images/base_3.png')
        alien = Alien(self.world,SCREEN_WIDTH,SCREEN_HEIGHT)
        #self.delta_x = alien.delta_x
        #self.delta_y = alien.delta_y
        self.delta_x = alien.change_x
        self.delta_y = alien.chnage_y
        self.is_on_jump = False
        self.checkyellowstar = True

        #self.alien.set_position(400, 125) #alien position
        

    def setup(self):
        self.background = arcade.load_texture("images/space2.jpg")
        self.base_list = arcade.SpriteList()
        self.yellowstar_list = arcade.SpriteList()
        self.blackstar_list = arcade.SpriteList()
        #self.alien_sprite.center_x = self.world.alien.x
        #self.alien_sprite.center_y = self.world.alien.y
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.world.alien.draw() 
        
        for base in self.world.base_list:
            base.draw()
        for yellowstar in self.world.yellowstar_list:
            yellowstar.draw()
        for blackstar in self.world.blackstar_list:
            blackstar.draw()

    def update(self,delta):
        self.world.update(delta)
        #self.alien_sprite.set_position(self.world.alien.x,self.world.alien.y)
        #self.base_sprite.set_position(self.world.base.x,self.world.base.y)  
        #self.world.alien.y -= self.delta_y*delta
        #self.world.alien.x += self.delta_x
        #self.world.base.y -= BASE_CONSTANT_Y*delta
        #self.world.base.x -= BASE_CONSTANT_X*delta #ถามเพื่อนว่าควรมีตรงนี้มั้ย
        #print(self.world.alien.center_y)
        #print(self.alien_sprite.center_y)
        #print(self.world.base.y)
        self.world.alien.change_x = self.delta_x
        #is_on_base = False
        
        for base in self.world.base_list:
            if self.world.alien.center_y >= base.center_y - 10.5 and self.world.alien.center_y <= base.center_y + 50.5 \
            and self.world.alien.center_x <= base.center_x + 65 and self.world.alien.center_x >= base.center_x - 65:
                    #self.delta_y *= -BOUNCINESS #แก้
                    #is_on_base = True
                self.is_on_jump = True
                self.world.alien.change_y = JUMP_CONSTANT
                #self.world.alien.change_y = 5
                break
        for yellowstar in self.world.yellowstar_list:
            if arcade.check_for_collision(self.world.alien,yellowstar):
                self.checkyellowstar = True
                yellowstar.kill()
                self.world.checkstar = 0
        for blackstar in self.world.blackstar_list:
            if arcade.check_for_collision(self.world.alien,blackstar):
                self.checkyellowstar = False
                blackstar.kill()
                self.world.checkstar = 0
        
        if self.is_on_jump:
            self.world.alien.change_y -= CHANGE_Y_CONSTANT
            if self.world.alien.change_y < -200: 
                self.is_on_jump = False
        else:
            self.world.alien.change_y = FALL_CONSTANT

        '''
        if(self.alien_sprite.center_y >= self.world.base.y-10.5 and self.alien_sprite.center_y <= self.world.base.y+50.5  and self.alien_sprite.center_x <= self.world.base.x+65 and self.alien_sprite.center_x >= self.world.base.x-65):
                #self.delta_y *= -BOUNCINESS #แก้
                self.delta_y = 0
                
        else:
            self.delta_y = GRAVITY_CONSTANT
        '''
        

    def on_key_press(self,key,modifiers):
        if(key == arcade.key.LEFT and self.checkyellowstar == True):
            self.delta_x = -MOVEMENT_CONSTANT
        elif(key == arcade.key.RIGHT and self.checkyellowstar == True):
            self.delta_x = MOVEMENT_CONSTANT
        elif(key == arcade.key.LEFT and self.checkyellowstar == False):
            self.delta_x = MOVEMENT_CONSTANT
        elif(key == arcade.key.RIGHT and self.checkyellowstar == False):
            self.delta_x = -MOVEMENT_CONSTANT
        
    def on_key_release(self,key,modifiers):
        if(key == arcade.key.LEFT or key == arcade.key.RIGHT):
           self.delta_x = 0
       
def main():
    window = AlienWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()      
