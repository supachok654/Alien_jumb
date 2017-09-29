import arcade
from random import randint
 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
class AlienWindow(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.BLUE)
 
def main():
    window = AlienWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()      
