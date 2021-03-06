import arcade
import arcade.key
from models import World,Alien,Base,YellowStar,BlackStar,Bullet,Asteroid,Heart
from random import randint
 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000
MOVEMENT_CONSTANT = 12
JUMP_CONSTANT = 20
FALL_CONSTANT = -10
CHANGE_Y_CONSTANT = 0.75
class AlienWindow(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width, height,"Alien Jump")
        self.background = None
        self.bullet_list = None
        self.world = World(width,height) 
        alien = Alien(self.world,SCREEN_WIDTH,SCREEN_HEIGHT)
        self.delta_x = alien.change_x
        self.delta_y = alien.chnage_y
        self.is_on_jump = False
        self.checkyellowstar = True
        self.alien_hp = 5
        self.checkalien = True
        self.game_over = False

    def setup(self):
        self.background = arcade.load_texture("images/space2.jpg")
        self.bullet_list = arcade.SpriteList()
        self.score = 0
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        for alien in self.world.alien_list:
            alien.draw()
        self.bullet_list.draw()
        for base in self.world.base_list:
            base.draw()
        for yellowstar in self.world.yellowstar_list:
            yellowstar.draw()
        for blackstar in self.world.blackstar_list:
            blackstar.draw()
        for bullet in self.world.bullet_list:
            bullet.draw()
        for asteroid in self.world.asteroid_list:
            asteroid.draw()
        for heart in self.world.heart_list:
            heart.draw()
        output = "Score: {}".format(self.score)
        arcade.draw_text(output,640,950,arcade.color.WHITE,20)
        output = "HP: {}".format(self.alien_hp)
        arcade.draw_text(output,640,975,arcade.color.WHITE,20)
        output = "Status: "
        arcade.draw_text(output,640,925,arcade.color.WHITE,20)
        if self.checkyellowstar:
            output = "Yellow"
            arcade.draw_text(output,720,925,arcade.color.YELLOW,20)
        else:
            output = "Black"
            arcade.draw_text(output,720,925,arcade.color.BLACK,20)
        if self.alien_hp <= 0 or self.world.alien.center_y < 0:
            self.draw_game_over()
            self.world.alien.kill()
            self.checkalien = False
    def update(self,delta):
        self.world.update(delta)
        self.world.alien.change_x = self.delta_x
        
        for base in self.world.base_list:
            if self.world.alien.center_y >= base.center_y - 10.5 and self.world.alien.center_y <= base.center_y + 50.5 \
            and self.world.alien.center_x <= base.center_x + 65 and self.world.alien.center_x >= base.center_x - 65 and self.world.alien.change_y < 0:
                self.is_on_jump = True
                if self.checkalien:
                    self.score += 10
                self.world.alien.change_y = JUMP_CONSTANT
                break
        for yellowstar in self.world.yellowstar_list:
            if arcade.check_for_collision(self.world.alien,yellowstar):
                self.checkyellowstar = True
                yellowstar.kill()
                self.world.checkstar = 0
                if self.checkalien:
                    self.score += 50
        for blackstar in self.world.blackstar_list:
            if arcade.check_for_collision(self.world.alien,blackstar):
                self.checkyellowstar = False
                blackstar.kill()
                if self.checkalien:
                    self.score += 100
                self.world.checkstar = 0

        for bullet in self.bullet_list:
            asteroids = arcade.check_for_collision_with_list(bullet, self.world.asteroid_list)
            if len(asteroids)>0:
                bullet.kill()
                for asteroid in asteroids:
                    asteroid.kill()
                    if self.checkalien:
                        self.score += 25
                    self.world.checkasteroid -= 1
        for enemy in self.world.asteroid_list:
            if arcade.check_for_collision(self.world.alien,enemy):
                if self.alien_hp > 0:
                    self.alien_hp -= 1
                enemy.kill()
                self.world.checkasteroid -= 1
        for heart in self.world.heart_list:
            if arcade.check_for_collision(self.world.alien,heart):
                self.world.checkheart = 0
                heart.kill()
                if self.alien_hp < 5:
                    self.alien_hp += 1
                   
        if self.is_on_jump:
            self.world.alien.change_y -= CHANGE_Y_CONSTANT
            if self.world.alien.change_y < -50: 
                self.is_on_jump = False
        else:
            self.world.alien.change_y = FALL_CONSTANT
        for bullet in self.bullet_list:
            bullet.update(delta)
            if(bullet.center_y > SCREEN_HEIGHT):
                bullet.kill()
                
    def draw_game_over(self):
        output = "Game Over"
        arcade.draw_text(output,250,650,arcade.color.WHITE,54)

        output = "Your Scores: {}".format(self.score)
        arcade.draw_text(output,300,600,arcade.color.WHITE,25)

    def on_key_press(self,key,modifiers):
        if key == arcade.key.LEFT and self.checkyellowstar == True:
            self.delta_x = -MOVEMENT_CONSTANT
        elif key == arcade.key.RIGHT and self.checkyellowstar == True:
            self.delta_x = MOVEMENT_CONSTANT
        elif key == arcade.key.LEFT and self.checkyellowstar == False:
            self.delta_x = MOVEMENT_CONSTANT
        elif key == arcade.key.RIGHT and self.checkyellowstar == False:
            self.delta_x = -MOVEMENT_CONSTANT
        if key == arcade.key.SPACE and self.checkalien:
            self.bullet_list.append(Bullet(self,self.world.alien.center_x,self.world.alien.center_y))
    def on_key_release(self,key,modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
           self.delta_x = 0
       
def main():
    window = AlienWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()      
