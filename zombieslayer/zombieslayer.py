#!/usr/bin/env python3

import arcade
from random import randint

screen_width = 800
screen_height = 600

class zombie_slayer(arcade.Window):
        space = False
        left_or_right = 0
        move_right = False
        move_left = False
        face_right = True
        face_left = False
        killed_zombies = ['','','','','']
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
        left_killed_zombies = ['','','','','']
        left_zombie_attack_true_or_false = [False,False,False,False,False]
        left_zombie_move_true_or_false = [False,False,False,False,False]
        left_zombie_disposal_count1 = 0
        left_zombie_disposal_count2 = 0
        left_zombie_disposal_count3 = 0
        left_zombie_disposal_count4 = 0
        left_zombie_disposal_count5 = 0
        left_zombie_disposal_count = [left_zombie_disposal_count1,left_zombie_disposal_count2,left_zombie_disposal_count3,left_zombie_disposal_count4,left_zombie_disposal_count5]
        left_dispose_of_zombie = [False,False,False,False,False]
        killed_zombies_combined = []
        left_my_zombie_list = []
        damage_points = 0
        attack_count = 0
        score = 0
        count_1 = 0
        count_2 = 0
        count_3 = 0
        zombie_count = 0
        zombie_count1 = 0
        left_zombie_count = 0
        left_zombie_count1 = 0
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
                self.left_zombie1_list = arcade.SpriteList()
                self.left_zombie_list = arcade.SpriteList()
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
                        self.zombie_sprite1 = arcade.Sprite("zombie1.png",0.44)
                        self.zombie_sprite1.center_x = 800
                        self.zombie_sprite1.center_y = 158
                        self.zombie1_list.append(self.zombie_sprite1)

                for i in range(5):
                        self.left_zombie_sprite = arcade.Sprite("left_zombie.png",0.44)
                        self.left_zombie_sprite.center_x = -100
                        self.left_zombie_sprite.center_y = 160
                        self.left_zombie_list.append(self.left_zombie_sprite)
                        self.left_my_zombie_list.append(self.left_zombie_sprite)

                for i in range(5):
                        self.left_zombie1_sprite = arcade.Sprite("left_zombie1.png",0.44)
                        self.left_zombie1_sprite.center_x = -90
                        self.left_zombie1_sprite.center_y = 160
                        self.left_zombie1_list.append(self.left_zombie1_sprite)

                self.player_zombie_sprite = arcade.Sprite("left_zombie.png",0.44)
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
                self.physics_engine11 = arcade.PhysicsEngineSimple(self.left_zombie_list[0],self.ground_list1)
                self.physics_engine12 = arcade.PhysicsEngineSimple(self.left_zombie_list[1],self.ground_list1)
                self.physics_engine13 = arcade.PhysicsEngineSimple(self.left_zombie_list[2],self.ground_list1)
                self.physics_engine14 = arcade.PhysicsEngineSimple(self.left_zombie_list[3],self.ground_list1)
                self.physics_engine15 = arcade.PhysicsEngineSimple(self.left_zombie_list[4],self.ground_list1)
                self.physics_engine16 = arcade.PhysicsEngineSimple(self.left_zombie1_list[0],self.ground_list1)
                self.physics_engine17 = arcade.PhysicsEngineSimple(self.left_zombie1_list[1],self.ground_list1)
                self.physics_engine18 = arcade.PhysicsEngineSimple(self.left_zombie1_list[2],self.ground_list1)
                self.physics_engine19 = arcade.PhysicsEngineSimple(self.left_zombie1_list[3],self.ground_list1)
                self.physics_engine20 = arcade.PhysicsEngineSimple(self.left_zombie1_list[4],self.ground_list1)
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
                        if self.face_right == True:
                                self.player_R_list.draw()
                        if self.face_left == True:
                                self.player_L_list.draw()
                
                elif self.space == True:
                        if self.face_right == True:
                                self.player_A_R_list.draw()
                        if self.face_left == True:
                                self.player_A_L_list.draw()
                        self.attack_count += 1
                        if self.attack_count == 13:
                                self.space = False
                                self.attack_count = 0

                for i in range(len(self.killed_zombies)):
                        if self.killed_zombies[i] != '': #and self.dispose_of_zombie[self.my_zombie_list.index(self.killed_zombies[i])] == False:
                                self.zombie1_list[self.my_zombie_list.index(self.killed_zombies[i])].draw()
                self.zombie_list.draw()
                
                for i in range(len(self.left_killed_zombies)):
                        if self.left_killed_zombies[i] != '':
                                self.left_zombie1_list[self.left_my_zombie_list.index(self.left_killed_zombies[i])].draw()
                self.left_zombie_list.draw()


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
                        self.move_right = True
                        self.move_left = False
                        self.face_right = True
                        self.face_left = False
                elif key == arcade.key.A: 
                                self.move_right = False
                                self.move_left = True
                                self.face_right = False
                                self.face_left = True


        def on_key_release(self,key,modifiers):
                if key == arcade.key.D:
                        self.move_right = False
                if key == arcade.key.A:
                        self.move_left = False

        def move_zombie(self):                       
                for i in range(len(self.zombie_move_true_or_false)):
                        #if i < len(self.zombie_list):
                                #if i < len(self.zombie1_list):
                                        if self.zombie_attack_true_or_false[i] == False and self.zombie_move_true_or_false[i] == True:
                                                if i == 1 or i == 4:
                                                        self.zombie_list[i].change_x = -4
                                                        self.zombie1_list[i].change_x = -4
                                                else:
                                                        self.zombie_list[i].change_x = -2
                                                        self.zombie1_list[i].change_x = -2
                                        else:
                                                self.zombie_list[i].change_x = 0
                                                self.zombie1_list[i].change_x = 0

                                        if self.killed_zombies[i] != '':
                                                self.zombie_list[self.my_zombie_list.index(self.killed_zombies[i])].center_x = 800
                                        if self.dispose_of_zombie[i] == True:
                                                self.zombie1_list[i].change_x = (800 - self.zombie1_list[i].center_x)
                                                self.dispose_of_zombie[i] = False
                                                
                for i in range(len(self.left_zombie_move_true_or_false)):
                        #if i < len(self.left_zombie_list):
                                #if i < len(self.zombie1_list):
                                        if self.left_zombie_attack_true_or_false[i] == False and self.left_zombie_move_true_or_false[i] == True:
                                                if i == 1 or i == 4:
                                                        self.left_zombie_list[i].change_x = 4
                                                        self.left_zombie1_list[i].change_x = 4
                                                else:
                                                        self.left_zombie_list[i].change_x = 2
                                                        self.left_zombie1_list[i].change_x = 2
                                        else:
                                                self.left_zombie_list[i].change_x = 0
                                                self.left_zombie1_list[i].change_x = 0

                                        if self.left_killed_zombies[i] != '':
                                                self.left_zombie_list[i].center_x = -100
                                        if self.left_dispose_of_zombie[i] == True:
                                                self.left_zombie1_list[i].change_x = (-100 - self.left_zombie1_list[i].center_x)
                                                self.left_dispose_of_zombie[i] = False
                
                self.left_or_right = randint(0,1)
                if self.left_or_right == 0:
                        if self.zombie_count1 != 5:
                                self.zombie_count += 1
                                if self.zombie_count%100 == 0:
                                        self.zombie_move_true_or_false[self.zombie_count1] = True
                                        self.zombie_count1 += 1
                else:
                        if self.left_zombie_count1 != 5:
                                self.left_zombie_count += 1
                                if self.left_zombie_count%100 == 0:
                                        self.left_zombie_move_true_or_false[self.left_zombie_count1] = True
                                        self.left_zombie_count1 += 1
        def move_player(self):
                if self.move_right == True:
                        self.player_R_sprite.change_x = 3
                        self.player_A_R_sprite.change_x = 3
                        self.player_zombie_sprite.change_x = 3
                        
                        self.player_L_sprite.change_x = 3
                        self.player_A_L_sprite.change_x = 3
                elif self.move_left == True:
                        self.player_R_sprite.change_x = -3
                        self.player_A_R_sprite.change_x = -3
                        self.player_zombie_sprite.change_x = -3

                        self.player_L_sprite.change_x = -3
                        self.player_A_L_sprite.change_x = -3
                else:
                        self.player_R_sprite.change_x = 0
                        self.player_A_R_sprite.change_x = 0
                        self.player_zombie_sprite.change_x = 0

                        self.player_L_sprite.change_x = 0
                        self.player_A_L_sprite.change_x = 0
                        

        def body_disposal(self):
                for i in range(len(self.killed_zombies)):
                        if self.killed_zombies[i] != '':
                                self.zombie_disposal_count[i] += 1
                                if self.zombie_disposal_count[i] == 120:
                                        self.dispose_of_zombie[self.my_zombie_list.index(self.killed_zombies[i])] = True
                                        self.zombie_move_true_or_false[self.my_zombie_list.index(self.killed_zombies[i])] = True
                                        self.killed_zombies[i] = ''
                                        self.zombie_disposal_count[i] = 0
                                        
                for i in range(len(self.left_killed_zombies)):
                        if self.left_killed_zombies[i] != '':
                                self.left_zombie_disposal_count[i] += 1
                                if self.left_zombie_disposal_count[i] == 120:
                                        self.left_dispose_of_zombie[self.left_my_zombie_list.index(self.left_killed_zombies[i])] = True
                                        self.left_zombie_move_true_or_false[self.left_my_zombie_list.index(self.left_killed_zombies[i])] = True
                                        self.left_killed_zombies[i] = ''
                                        self.left_zombie_disposal_count[i] = 0


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
                        zombie_slayer.move_player(self)
                        zombie_slayer.update_my_physics_engine(self)
                        

                        if self.space == True:
                                if self.face_right == True:
                                        self.kill_zombie = arcade.check_for_collision_with_list(self.player_A_R_sprite,self.zombie_list)
                                        for i in self.kill_zombie:
                                                self.killed_zombies[self.my_zombie_list.index(i)] = i
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
                                        if self.zombie_attack_true_or_false[i] == True and self.killed_zombies[i] == '':
                                                self.damage_points += 4

                "***********************************************************"
                if self.game_over == False:        
                        zombie_slayer.body_disposal(self)
                        
                        if self.damage_points > 0:
                                self.damage_points -= 1

                        if self.space == True:
                                if self.face_right == False:
                                        self.kill_zombie = arcade.check_for_collision_with_list(self.player_A_L_sprite,self.left_zombie_list)
                                        for i in self.kill_zombie:
                                                self.left_killed_zombies[self.left_my_zombie_list.index(i)] = i
                                                self.left_zombie_move_true_or_false[self.left_my_zombie_list.index(i)] = False

                        elif self.space == False:
                                zombie_attack_list1 = arcade.check_for_collision_with_list(self.player_L_sprite,self.left_zombie_list)
                                
                                for i in zombie_attack_list1:   
                                        self.left_zombie_attack_true_or_false[self.left_my_zombie_list.index(i)] = True
                                        
                                if len(zombie_attack_list1) == 0:
                                        for i in range(len(self.left_zombie_attack_true_or_false)):
                                                self.left_zombie_attack_true_or_false[i] = False
                                else:
                                        for i in range(len(self.left_zombie_attack_true_or_false)):
                                                if self.left_zombie_attack_true_or_false[i] == True:
                                                        if self.left_my_zombie_list[i] in zombie_attack_list:
                                                                self.left_zombie_attack_true_or_false[i] == True
                                                        else:
                                                                self.left_zombie_attack_true_or_false[i] == False
                                                
                                for i in range(len(self.left_zombie_attack_true_or_false)):
                                        if self.left_zombie_attack_true_or_false[i] == True and self.left_killed_zombies[i] == '':
                                                self.damage_points += 4

                if self.damage_points >= 900:
                        self.game_over = False
                        self.you_lose = True
                self.killed_zombies_combined = [] + self.killed_zombies + self.left_killed_zombies
                for i in self.killed_zombies_combined:
                        if i == True:
                                self.score += 1
                                if self.score == 10:
                                        self.you_win = False
                self.score = 0
                "***********************************************************"
                

def main():     
        game = zombie_slayer(screen_width,screen_height)
        game.setup()
        arcade.run()
        
if __name__ == "__main__":
        main()
