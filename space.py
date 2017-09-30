import arcade
from random import randint
 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000
class AlienWindow(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width, height)
        self.background = None
        self.alien = arcade.Sprite('images/alien1.png')
        self.alien.set_position(400, 125)
        
    def setup(self):
        self.background = arcade.load_texture("images/space2.jpg")
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.alien.draw()
def main():
    window = AlienWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()      
