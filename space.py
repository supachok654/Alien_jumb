import arcade
from models import World,Alien
from random import randint
 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000
GRAVITY_CONSTANT = 750

class AlienWindow(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width, height)
        self.background = None
        self.world = World(width,height)
        self.alien_sprite = arcade.Sprite('images/alien1.png')
        #self.alien.set_position(400, 125) #alien position
        #self.playerx = 400
        #self.playery = 850

    def setup(self):
        self.background = arcade.load_texture("images/space2.jpg")
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.alien_sprite.draw()
    def update(self,delta):
        self.world.update(delta)
        self.alien_sprite.set_position(self.world.alien.x,self.world.alien.y)
        self.world.alien.y -= GRAVITY_CONSTANT*delta
        print(self.world.alien.y)
def main():
    window = AlienWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()      
