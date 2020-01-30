#!/usr/bin/env python3

import arcade
from random import randint

screen_width = 800
screen_height = 600


class zombie_slayer(arcade.Window):
        space = False
        d = False
        a = False
        left_or_right = 0
        move_right = True
        move_left = False
        killed_zombies = [False,False,False,False,False]
        zombie_attack_true_or_false = [False,False,False,False,False]
        zombie_move_true_or_false = [False,False,False,False,False]
        zombie_disposal_count1 = 0
        zombie_disposal_count2 = 0
        zombie_disposal_count3 = 0
        zombie_disposal_count4 = 0
        zombie_disposal_count5 = 0
        zombie_disposal_count = [zombie_disposal_count1,zombie_disposal_count2,zombie_disposal_count3,zombie_disposal_count4,zombie_disposal_count5]
        dispose_of_zombie = [False,False,False,False,False]
        my_zombie_list = []
        killed_zombies1 = [False,False,False,False,False]
        zombie_attack_true_or_false1 = [False,False,False,False,False]
        zombie_move_true_or_false1 = [False,False,False,False,False]
        zombie_disposal1_count1 = 0
        zombie_disposal1_count2 = 0
        zombie_disposal1_count3 = 0
        zombie_disposal1_count4 = 0
        zombie_disposal1_count5 = 0
        zombie_disposal1_count = [zombie_disposal1_count1,zombie_disposal1_count2,zombie_disposal1_count3,zombie_disposal1_count4,zombie_disposal1_count5]
        dispose_of_zombie1 = [False,False,False,False,False]
        killed_zombies_combined = []
        my_zombie_list1 = []
        damage_points = 0
        attack_count = 0
        score = 0
        count_1 = 0
        count_2 = 0
        count_3 = 0
        zombie_count = 0
        zombie_count1 = 0
        inv_zombie_count = 0
        inv_zombie_count1 = 0
        game_over = False
        you_lose = False
        you_win = False
        attack_delay = 0
        attack_delay_true_or_false = False
        
        def __init__(self,width,height):
                super().__init__(width,height,"STICKMAN ZOMBIESLAYER")
                
                arcade.set_background_color(arcade.color.CORNFLOWER_BLUE)
                
        def setup(self):
                self.player_R_list = arcade.SpriteList()
                self.player_A_R_list = arcade.SpriteList()
                self.player_L_list = arcade.SpriteList()
                self.player_A_L_list = arcade.SpriteList()
                self.ground_list = arcade.SpriteList()
                self.ground_list1 = arcade.SpriteList()
                self.zombie_list = arcade.SpriteList()
                self.zombie1_list = arcade.SpriteList()
                self.player_zombie_list = arcade.SpriteList()
                self.inv_zombie1_list = arcade.SpriteList()
                self.inv_zombie_list = arcade.SpriteList()
                self.player_health_list = arcade.SpriteList()
                self.health_bar_list = arcade.SpriteList()
                self.game_over_list = arcade.SpriteList()
                self.you_win_list = arcade.SpriteList()

                count_1 = -75
                for i in range(9):
                        self.ground_sprite = arcade.Sprite("/home/elliot/.local/lib64/python3.6/site-packages/arcade/resources/images/tiles/grassHalf_mid.png")
                        if i == 0:
                                self.ground_sprite.center_x = -65
                                self.ground_sprite.center_y = 80
                        elif i == 8:
                                self.ground_sprite.center_x = 865
                                self.ground_sprite.center_y = 80
                        else:  
                                self.ground_sprite.center_x = count_1
                                self.ground_sprite.center_y = 10

                        self.ground_list.append(self.ground_sprite)

                        count_1 += 125

                count_1 = -75
                for i in range(9):
                        self.ground_sprite = arcade.Sprite("/home/elliot/.local/lib64/python3.6/site-packages/arcade/resources/images/tiles/grassHalf_mid.png")

                        self.ground_sprite.center_x = count_1
                        self.ground_sprite.center_y = 10

                        self.ground_list1.append(self.ground_sprite)

                        count_1 += 125

                count_2 = 200
                for i in range(10):
                        self.health_bar_sprite = arcade.Sprite("/home/elliot/Documents/python/arcade/hb.png",0.5)

                        self.health_bar_sprite.center_x = count_2
                        self.health_bar_sprite.center_y = 505

                        self.health_bar_list.append(self.health_bar_sprite)

                        count_2 += 20

                self.player_health = arcade.Sprite("/home/elliot/Documents/python/arcade/hp.png",0.5)
                self.player_health.center_x = 155
                self.player_health.center_y = 520
                self.player_health_list.append(self.player_health)
                
                self.player_R_sprite = arcade.Sprite("/home/elliot/Documents/python/arcade/stickman_R.png",0.5)
                self.player_R_sprite.center_x = 400
                self.player_R_sprite.center_y = 165
                self.player_R_list.append(self.player_R_sprite)
                self.player_A_R_sprite = arcade.Sprite("/home/elliot/Documents/python/arcade/stickman_A_R.png",0.5)
                self.player_A_R_sprite.center_x = 455
                self.player_A_R_sprite.center_y = 170
                self.player_A_R_list.append(self.player_A_R_sprite)

                self.player_L_sprite = arcade.Sprite("/home/elliot/Documents/python/arcade/stickman_L.png",0.5)
                self.player_L_sprite.center_x = 400
                self.player_L_sprite.center_y = 165
                self.player_L_list.append(self.player_L_sprite)
                self.player_A_L_sprite = arcade.Sprite("/home/elliot/Documents/python/arcade/stickman_A_L.png",0.5)
                self.player_A_L_sprite.center_x = 330
                self.player_A_L_sprite.center_y = 170
                self.player_A_L_list.append(self.player_A_L_sprite)

                for i in range(5):
                        self.zombie_sprite = arcade.Sprite("/home/elliot/Documents/python/arcade/zombie.png",0.44)
                        self.zombie_sprite.center_x = 800
                        self.zombie_sprite.center_y = 158
                        self.zombie_list.append(self.zombie_sprite)
                        self.my_zombie_list.append(self.zombie_sprite)
                
                for i in range(5):
                        self.zombie_sprite1 = arcade.Sprite("/home/elliot/Documents/python/arcade/zombie1.png",0.44)
                        self.zombie_sprite1.center_x = 800
                        self.zombie_sprite1.center_y = 158
                        self.zombie1_list.append(self.zombie_sprite1)

                for i in range(5):
                        self.inv_zombie_sprite = arcade.Sprite("/home/elliot/Documents/python/arcade/inv_zombie.png",0.44)
                        self.inv_zombie_sprite.center_x = -50
                        self.inv_zombie_sprite.center_y = 160
                        self.inv_zombie_list.append(self.inv_zombie_sprite)
                        self.my_zombie_list1.append(self.inv_zombie_sprite)

                for i in range(5):
                        self.inv_zombie1_sprite = arcade.Sprite("/home/elliot/Documents/python/arcade/inv_zombie1.png",0.44)
                        self.inv_zombie1_sprite.center_x = -40
                        self.inv_zombie1_sprite.center_y = 160
                        self.inv_zombie1_list.append(self.inv_zombie1_sprite)

                self.player_zombie_sprite = arcade.Sprite("/home/elliot/Documents/python/arcade/inv_zombie.png",0.44)
                self.player_zombie_sprite.center_x = 385
                self.player_zombie_sprite.center_y = 160
                self.player_zombie_list.append(self.player_zombie_sprite)


                self.game_over_sprite = arcade.Sprite("/home/elliot/Documents/python/arcade/game_over.png")
                self.game_over_sprite.center_x = 400
                self.game_over_sprite.center_y = 420
                self.game_over_list.append(self.game_over_sprite)

                self.you_win_sprite = arcade.Sprite("/home/elliot/Documents/python/arcade/you_win.png")
                self.you_win_sprite.center_x = 400
                self.you_win_sprite.center_y = 420
                self.you_win_list.append(self.you_win_sprite)
                
                self.physics_engine1 = arcade.PhysicsEngineSimple(self.zombie_list[0],self.ground_list1)
                self.physics_engine2 = arcade.PhysicsEngineSimple(self.zombie_list[1],self.ground_list1)
                self.physics_engine3 = arcade.PhysicsEngineSimple(self.zombie_list[2],self.ground_list1)
                self.physics_engine4 = arcade.PhysicsEngineSimple(self.zombie_list[3],self.ground_list1)
                self.physics_engine5 = arcade.PhysicsEngineSimple(self.zombie_list[4],self.ground_list1)
                self.physics_engine6 = arcade.PhysicsEngineSimple(self.zombie1_list[0],self.ground_list1)
                self.physics_engine7 = arcade.PhysicsEngineSimple(self.zombie1_list[1],self.ground_list1)
                self.physics_engine8 = arcade.PhysicsEngineSimple(self.zombie1_list[2],self.ground_list1)
                self.physics_engine9 = arcade.PhysicsEngineSimple(self.zombie1_list[3],self.ground_list1)
                self.physics_engine10 = arcade.PhysicsEngineSimple(self.zombie1_list[4],self.ground_list1)
                self.physics_engine11 = arcade.PhysicsEngineSimple(self.inv_zombie_list[0],self.ground_list1)
                self.physics_engine12 = arcade.PhysicsEngineSimple(self.inv_zombie_list[1],self.ground_list1)
                self.physics_engine13 = arcade.PhysicsEngineSimple(self.inv_zombie_list[2],self.ground_list1)
                self.physics_engine14 = arcade.PhysicsEngineSimple(self.inv_zombie_list[3],self.ground_list1)
                self.physics_engine15 = arcade.PhysicsEngineSimple(self.inv_zombie_list[4],self.ground_list1)
                self.physics_engine16 = arcade.PhysicsEngineSimple(self.inv_zombie1_list[0],self.ground_list1)
                self.physics_engine17 = arcade.PhysicsEngineSimple(self.inv_zombie1_list[1],self.ground_list1)
                self.physics_engine18 = arcade.PhysicsEngineSimple(self.inv_zombie1_list[2],self.ground_list1)
                self.physics_engine19 = arcade.PhysicsEngineSimple(self.inv_zombie1_list[3],self.ground_list1)
                self.physics_engine20 = arcade.PhysicsEngineSimple(self.inv_zombie1_list[4],self.ground_list1)
                self.physics_engine21 = arcade.PhysicsEngineSimple(self.player_R_sprite,self.ground_list)
                self.physics_engine22 = arcade.PhysicsEngineSimple(self.player_A_R_sprite,self.ground_list)
                self.physics_engine23 = arcade.PhysicsEngineSimple(self.player_L_sprite,self.ground_list)
                self.physics_engine24 = arcade.PhysicsEngineSimple(self.player_A_L_sprite,self.ground_list)
                self.physics_engine25 = arcade.PhysicsEngineSimple(self.player_zombie_sprite,self.ground_list)



        def on_draw(self):
                arcade.start_render()

                if self.you_lose == True:
                        self.game_over_list.draw()
                        self.player_zombie_list.draw()
                        
                if self.you_win == True:
                        self.you_win_list.draw()
                        
                if self.space == False and self.you_lose != True:
                        if self.move_right == True:
                                self.player_R_list.draw()
                        if self.move_left == True:
                                self.player_L_list.draw()
                
                elif self.space == True:
                        if self.move_right == True:
                                self.player_A_R_list.draw()
                        if self.move_left == True:
                                self.player_A_L_list.draw()
                        self.attack_count += 1
                        if self.attack_count == 10:
                                self.space = False
                                self.attack_count = 0

                
                for i in range(len(self.killed_zombies)):
                        if self.killed_zombies[i] == True and self.dispose_of_zombie[i] == False:
                                self.zombie1_list[i].draw()
                        if self.killed_zombies[i] == False:
                                self.zombie_list[i].draw()
                for i in range(len(self.killed_zombies1)):
                        if self.killed_zombies1[i] == True and self.dispose_of_zombie1[i] == False:
                                self.inv_zombie1_list[i].draw()
                        if self.killed_zombies1[i] == False:
                                self.inv_zombie_list[i].draw()


                self.ground_list.draw()
                self.player_health_list.draw()

                if self.damage_points < 50:
                        self.health_bar_list.draw()
                elif self.damage_points > 50 and self.damage_points < 100:
                        for i in range(len(self.health_bar_list)-1):
                                self.health_bar_list[i].draw()
                elif self.damage_points > 100 and self.damage_points < 200:
                        for i in range(len(self.health_bar_list)-2):
                                self.health_bar_list[i].draw()
                elif self.damage_points > 200 and self.damage_points < 300:
                        for i in range(len(self.health_bar_list)-3):
                                self.health_bar_list[i].draw()
                elif self.damage_points > 300 and self.damage_points < 400:
                        for i in range(len(self.health_bar_list)-4):
                                self.health_bar_list[i].draw()
                elif self.damage_points > 400 and self.damage_points < 500:
                        for i in range(len(self.health_bar_list)-5):
                                self.health_bar_list[i].draw()
                elif self.damage_points > 500 and self.damage_points < 600:
                        for i in range(len(self.health_bar_list)-6):
                                self.health_bar_list[i].draw()
                elif self.damage_points > 600 and self.damage_points < 700:
                        for i in range(len(self.health_bar_list)-7):
                                self.health_bar_list[i].draw()
                elif self.damage_points > 700 and self.damage_points < 800:
                        for i in range(len(self.health_bar_list)-8):
                                self.health_bar_list[i].draw()
                elif self.damage_points > 800 and self.damage_points < 900:
                        for i in range(len(self.health_bar_list)-9):
                                self.health_bar_list[i].draw()
                elif self.damage_points == 900:
                        self.game_over = True

                                

        def on_key_press(self,key,modifiers):
                if key == arcade.key.SPACE:
                        if self.attack_delay_true_or_false == False:
                                self.space = True
                                self.attack_delay_true_or_false = True
                if key == arcade.key.D:
                        self.player_R_sprite.change_x = 3
                        self.player_A_R_sprite.change_x = 3
                        self.player_zombie_sprite.change_x = 3
                        
                        self.player_L_sprite.change_x = 3
                        self.player_A_L_sprite.change_x = 3
                        
                        self.move_right = True
                        self.move_left = False
                elif key == arcade.key.A:
                        #if self.player_L_sprite.center_x > 200:
                                self.player_R_sprite.change_x = -3
                                self.player_A_R_sprite.change_x = -3
                                self.player_zombie_sprite.change_x = -3

                                self.player_L_sprite.change_x = -3
                                self.player_A_L_sprite.change_x = -3
                                
                                self.move_right = False
                                self.move_left = True


        def on_key_release(self,key,modifiers):
                if key == arcade.key.D or key == arcade.key.A:
                                self.player_R_sprite.change_x = 0
                                self.player_A_R_sprite.change_x = 0
                                self.player_zombie_sprite.change_x = 0

                                self.player_L_sprite.change_x = 0
                                self.player_A_L_sprite.change_x = 0


        def move_zombie(self):                       
                for i in range(len(self.zombie_move_true_or_false)):
                        if i < len(self.zombie_list):
                                #if i < len(self.zombie1_list):
                                        if self.zombie_attack_true_or_false[i] == False and self.zombie_move_true_or_false[i] == True:
                                                if i == 1 or i == 4:
                                                        self.zombie_list[i].change_x = -4
                                                else:
                                                        self.zombie_list[i].change_x = -2
                                        else:
                                                self.zombie_list[i].change_x = 0
                                                        
                                        if self.zombie_move_true_or_false[i] == True and self.zombie_attack_true_or_false[i] == False:
                                                if i == 1 or i == 4:
                                                        self.zombie1_list[i].change_x = -4
                                                else:
                                                        self.zombie1_list[i].change_x = -2
                                        else:
                                                self.zombie1_list[i].change_x = 0
                                                
                for i in range(len(self.zombie_move_true_or_false1)):
                        if i < len(self.inv_zombie_list):
                                #if i < len(self.zombie1_list):
                                        if self.zombie_attack_true_or_false1[i] == False and self.zombie_move_true_or_false1[i] == True:
                                                if i == 1 or i == 4:
                                                        self.inv_zombie_list[i].change_x = 4
                                                else:
                                                        self.inv_zombie_list[i].change_x = 2
                                        else:
                                                self.inv_zombie_list[i].change_x = 0
                                                        
                                        if self.zombie_move_true_or_false1[i] == True and self.zombie_attack_true_or_false1[i] == False:
                                                if i == 1 or i == 4:
                                                        self.inv_zombie1_list[i].change_x = 4
                                                else:
                                                        self.inv_zombie1_list[i].change_x = 2
                                        else:
                                                self.inv_zombie1_list[i].change_x = 0
                
                self.left_or_right = randint(0,1)
                if self.left_or_right == 0:
                        if self.zombie_count1 != 5:
                                self.zombie_count += 1
                                if self.zombie_count%100 == 0:
                                        self.zombie_move_true_or_false[self.zombie_count1] = True
                                        self.zombie_count1 += 1
                else:
                        if self.inv_zombie_count1 != 5:
                                self.inv_zombie_count += 1
                                if self.inv_zombie_count%100 == 0:
                                        self.zombie_move_true_or_false1[self.inv_zombie_count1] = True
                                        self.inv_zombie_count1 += 1


        def body_disposal(self):
                for i in range(len(self.killed_zombies)):
                        if self.killed_zombies[i] == True:
                                self.zombie_disposal_count[i] += 1
                                if self.zombie_disposal_count[i] == 120:
                                        self.dispose_of_zombie[i] = True
                                        
                for i in range(len(self.killed_zombies1)):
                        if self.killed_zombies1[i] == True:
                                self.zombie_disposal1_count[i] += 1
                                if self.zombie_disposal1_count[i] == 120:
                                        self.dispose_of_zombie1[i] = True


        def update_my_physics_engine(self):
                self.physics_engine1.update()
                self.physics_engine2.update()
                self.physics_engine3.update()
                self.physics_engine4.update()
                self.physics_engine5.update()
                self.physics_engine6.update()
                self.physics_engine7.update()
                self.physics_engine8.update()
                self.physics_engine9.update()
                self.physics_engine10.update()
                self.physics_engine11.update()
                self.physics_engine12.update()
                self.physics_engine13.update()
                self.physics_engine14.update()
                self.physics_engine15.update()
                self.physics_engine16.update()
                self.physics_engine17.update()
                self.physics_engine18.update()
                self.physics_engine19.update()
                self.physics_engine20.update()
                self.physics_engine21.update()
                self.physics_engine22.update()
                self.physics_engine23.update()
                self.physics_engine24.update()
                self.physics_engine25.update()
                        
                
        def update(self,delta_time):                                
                if self.attack_delay_true_or_false == True:
                        self.attack_delay += 1
                        if self.attack_delay == 25:
                                self.attack_delay = 0
                                self.attack_delay_true_or_false = False
                
                if self.player_A_L_sprite.center_x != self.player_L_sprite.center_x - 70:
                        self.player_A_L_sprite.change_x = (self.player_L_sprite.center_x - 70) - self.player_A_L_sprite.center_x
                if self.player_A_R_sprite.center_x != self.player_R_sprite.center_x + 55:
                        self.player_A_R_sprite.change_x = (self.player_R_sprite.center_x + 55) - self.player_A_R_sprite.center_x
                                
                if self.game_over == False:        
                        zombie_slayer.body_disposal(self)
                        
                        if self.damage_points > 0:
                                self.damage_points -= 1
                                
                        zombie_slayer.move_zombie(self)
                        zombie_slayer.update_my_physics_engine(self)
                        

                        if self.space == True:
                                self.kill_zombie = arcade.check_for_collision_with_list(self.player_A_R_sprite,self.zombie_list)
                                for i in self.kill_zombie:
                                        self.killed_zombies[self.my_zombie_list.index(i)] = True
                                        self.zombie_move_true_or_false[self.my_zombie_list.index(i)] = False

                        elif self.space == False:
                                zombie_attack_list = arcade.check_for_collision_with_list(self.player_R_sprite,self.zombie_list)
                                
                                for i in zombie_attack_list:   
                                        self.zombie_attack_true_or_false[self.my_zombie_list.index(i)] = True
                                        
                                if len(zombie_attack_list) == 0:
                                        for i in range(len(self.zombie_attack_true_or_false)):
                                                self.zombie_attack_true_or_false[i] = False
                                else:
                                        for i in range(len(self.zombie_attack_true_or_false)):
                                                if self.zombie_attack_true_or_false[i] == True:
                                                        if self.my_zombie_list[i] in zombie_attack_list:
                                                                self.zombie_attack_true_or_false[i] == True
                                                        else:
                                                                self.zombie_attack_true_or_false[i] == False
                                                
                                for i in range(len(self.zombie_attack_true_or_false)):
                                        if self.zombie_attack_true_or_false[i] == True and self.killed_zombies[i] == False:
                                                self.damage_points += 4

                "***********************************************************"
                if self.game_over == False:        
                        zombie_slayer.body_disposal(self)
                        
                        if self.damage_points > 0:
                                self.damage_points -= 1
                        

                        if self.space == True:
                                self.kill_zombie = arcade.check_for_collision_with_list(self.player_A_L_sprite,self.inv_zombie_list)
                                for i in self.kill_zombie:
                                        self.killed_zombies1[self.my_zombie_list1.index(i)] = True
                                        self.zombie_move_true_or_false1[self.my_zombie_list1.index(i)] = False

                        elif self.space == False:
                                zombie_attack_list1 = arcade.check_for_collision_with_list(self.player_L_sprite,self.inv_zombie_list)
                                
                                for i in zombie_attack_list1:   
                                        self.zombie_attack_true_or_false1[self.my_zombie_list1.index(i)] = True
                                        
                                if len(zombie_attack_list1) == 0:
                                        for i in range(len(self.zombie_attack_true_or_false1)):
                                                self.zombie_attack_true_or_false1[i] = False
                                else:
                                        for i in range(len(self.zombie_attack_true_or_false1)):
                                                if self.zombie_attack_true_or_false1[i] == True:
                                                        if self.my_zombie_list1[i] in zombie_attack_list:
                                                                self.zombie_attack_true_or_false1[i] == True
                                                        else:
                                                                self.zombie_attack_true_or_false1[i] == False
                                                
                                for i in range(len(self.zombie_attack_true_or_false1)):
                                        if self.zombie_attack_true_or_false1[i] == True and self.killed_zombies1[i] == False:
                                                self.damage_points += 4

                if self.damage_points >= 900:
                        self.game_over = True
                        self.you_lose = True
                self.killed_zombies_combined = [] + self.killed_zombies + self.killed_zombies1
                for i in self.killed_zombies_combined:
                        if i == True:
                                self.score += 1
                                if self.score == 10:
                                        self.you_win = True
                self.score = 0
                "***********************************************************"
                

def main():     
        game = zombie_slayer(screen_width,screen_height)
        game.setup()
        arcade.run()
        
if __name__ == "__main__":
        main()