#!/usr/bin/env python3

import arcade,math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    uni_scale_factor = 0
    cycle = 0
    time = 0
    scale_factor = 1/18
    helike_up = False
    helike_down = False
    hight_value = '0'
    velocity_value = '0'
    angle_value = '0'
    selection_value = '0'
    r = False
    space = False
    enter = False
    
    helike_rad = 100
    helike_center_x = 400
    helike_center_y = 300
    
    line_x = 0
    line_y = 0
    line_x2 = 0
    line_y2 = 0
    line_angle = 90
    north_pole_x = 0
    north_pole_y = 0
    angle_up = False
    angle_down = False
    leg1_start = [0,0]
    leg1_end = [0,0]
    leg2_start = [0,0]
    leg2_end = [0,0]
    leg_change_x = 20
    leg_change_y = 40
    body_start = [0,0]
    body_end = [0,0]
    body_change = 50
    body_width = 5
    arm_start = [0,0]
    arm_end = [0,0]
    arm_height = 25
    arm_len = 35
    head_center_x = 0
    head_center_y = 0
    head_rad = 20
    north_pole_scale = 200

    gravity_constant = 6750000
    projectile_rad = 10
    projectile_x = helike_center_x + 0
    projectile_y = helike_center_y + projectile_rad + helike_rad
    projectile_y1 = projectile_y
    projectile_force_x = 0
    projectile_force_y = 0
    projectile_distance_from_center = 2100
    projectile_velocity = 0
    projectile_angle = 0
    projectile_velocity1 = 0
    projectile_velocity_x = 0
    projectile_velocity_y = 0
    projectile_acc_x = 0
    projectile_acc_y = 0

    force_on_projectile = 0

    tangent_angle = 0

    set_up = True

    selection = 0

    a = 0
    b = 0


    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        pass

    def on_draw(self):
        """ Render the screen. """
        
        arcade.start_render()

        if self.set_up == True:
            if self.selection == 0:
                arcade.draw_text("Hight: {}".format(round(self.projectile_y,1)-self.helike_center_y-self.projectile_rad-self.helike_rad),10,580,arcade.color.RED,12)
            else:
                arcade.draw_text("Hight: {}".format(round(self.projectile_y,1)-self.helike_center_y-self.projectile_rad-self.helike_rad),10,580,arcade.color.WHITE,12)
            if self.selection == 1:
                arcade.draw_text("Velocitiy: {}".format(round(self.projectile_velocity,1)),110,580,arcade.color.RED,12)
            else:
                arcade.draw_text("Velocitiy: {}".format(round(self.projectile_velocity,1)),110,580,arcade.color.WHITE,12)
            if self.selection == 2:
                arcade.draw_text("Angle: {}".format(round(self.projectile_angle,1)),250,580,arcade.color.RED,12)
            else:
                arcade.draw_text("Angle: {}".format(round(self.projectile_angle,1)),250,580,arcade.color.WHITE,12)


        arcade.draw_circle_filled(self.helike_center_x, self.helike_center_y, self.helike_rad, arcade.color.GREEN)
        #arcade.draw_line(self.line_x,self.line_y,self.line_x2,self.line_y2, arcade.color.RED,5)
        #arcade.draw_line(self.leg1_start[0],self.leg1_start[1],self.leg1_end[0],self.leg1_end[1],arcade.color.WHITE,self.body_width)
        #arcade.draw_line(self.leg2_start[0],self.leg2_start[1],self.leg2_end[0],self.leg2_end[1],arcade.color.WHITE,self.body_width)
        #arcade.draw_line(self.body_start[0],self.body_start[1],self.body_end[0],self.body_end[1],arcade.color.WHITE,self.body_width)
        #arcade.draw_line(self.arm_start[0],self.arm_start[1],self.arm_end[0],self.arm_end[1],arcade.color.WHITE,self.body_width)
        #arcade.draw_circle_outline(self.head_center_x,self.head_center_y,self.head_rad,arcade.color.WHITE,self.body_width,100)
        arcade.draw_circle_filled(self.projectile_x,self.projectile_y,self.projectile_rad,arcade.color.RED)
        #arcade.draw_line(self.tangent_x,self.tangent_y,self.tangent_x2,self.tangent_y2,arcade.color.RED,2)
        
        arcade.finish_render
        
    def on_key_press(self,key,modifiers):
        if key == arcade.key.UP:
            self.helike_up = True
        if key == arcade.key.DOWN:
            self.helike_down = True
        if key == arcade.key.LEFT:
            self.angle_up = True
        if key == arcade.key.RIGHT:
            self.angle_down = True
        if key == arcade.key.SPACE and self.space == False:
            self.space = True
        if key == arcade.key.ENTER and self.enter == False:
            self.enter = True
        if key == arcade.key.R:
            self.r = True
            
        if key == arcade.key.LEFT:
            self.selection -= 1
            self.selection_value = '0'
            if self.selection == -1:
                self.selection = 2
                
        if key == arcade.key.RIGHT:
            self.selection += 1
            self.selection_value = '0'
            if self.selection == 3:
                self.selection = 0
                
        if key == arcade.key.NUM_0:
            self.selection_value = '0' + self.selection_value + '0'
        if key == arcade.key.NUM_1:
            self.selection_value = '0' +  self.selection_value + '1'
        if key == arcade.key.NUM_2:
            self.selection_value = '0' +  self.selection_value + '2'
        if key == arcade.key.NUM_3:
            self.selection_value = '0' +  self.selection_value + '3'
        if key == arcade.key.NUM_4:
            self.selection_value = '0' +  self.selection_value + '4'
        if key == arcade.key.NUM_5:
            self.selection_value = '0' +  self.selection_value + '5'
        if key == arcade.key.NUM_6:
            self.selection_value = '0' +  self.selection_value + '6'
        if key == arcade.key.NUM_7:
            self.selection_value = '0' +  self.selection_value + '7'
        if key == arcade.key.NUM_8:
            self.selection_value = '0' +  self.selection_value + '8'
        if key == arcade.key.NUM_9:
            self.selection_value = '0' +  self.selection_value + '9'

        if key == arcade.key.DELETE:
            self.selection_value = '0'
    

    def on_key_release(self,key,modifiers): 
        if key == arcade.key.UP:
            self.helike_up = False
        if key == arcade.key.DOWN:
            self.helike_down = False
        if key == arcade.key.LEFT:
            self.angle_up = False
        if key == arcade.key.RIGHT:
            self.angle_down = False
        if key == arcade.key.SPACE:
            self.space = False
        if key == arcade.key.ENTER:
            self.enter = False
        if key == arcade.key.R:
            self.r = False


    def update(self, delta_time):
        print(delta_time)
        
        self.time = delta_time

        if self.set_up == True:
            if self.helike_up == True and self.selection == 0:   
                self.selection_value = str(int(self.selection_value) + 1)
            if self.helike_down == True and self.selection == 0 and int(self.selection_value) > 0:
                self.selection_value = str(int(self.selection_value) - 1)#self.projectile_y -= 1
            if self.helike_up == True and self.selection == 1:
                self.selection_value = str(int(self.selection_value) + 1)#self.projectile_velocity += 1
            if self.helike_down == True and self.selection == 1 and int(self.selection_value) > 0:
                self.selection_value = str(int(self.selection_value) - 1)#self.projectile_velocity -= 1
            if self.helike_up == True and self.selection == 2:
                self.selection_value = str(int(self.selection_value) + 1)#self.projectile_angle += 1
            if self.helike_down == True and self.selection == 2 and int(self.selection_value) > 0:
                self.selection_value = str(int(self.selection_value) - 1)#self.projectile_angle -= 1

            if self.selection == 0:
                self.projectile_y = self.helike_center_y + self.projectile_rad + self.helike_rad + int(self.selection_value)
            if self.selection == 1:
                self.projectile_velocity = int(self.selection_value)
            if self.selection == 2:
                self.projectile_angle = int(self.selection_value)
                
            self.projectile_velocity_x = self.projectile_velocity*math.cos(math.radians(self.projectile_angle))
            self.projectile_velocity_y = self.projectile_velocity*math.sin(math.radians(self.projectile_angle))
            
            if self.space == True or self.enter == True:
                self.set_up = False
    
        else:

            if self.r == True:
                self.set_up = True
                self.projectile_x = 400
                self.projectile_y = self.helike_center_y + self.projectile_rad + self.helike_rad
                self.projectile_velocity = 0
                self.projectile_angle = 0
                self.selection = 0
                self.selection_value = '0'
                MyGame.update(self,delta_time)

            self.north_pole_x = self.helike_center_x
            self.norht_pole_y = self.helike_center_y + self.helike_rad

            self.leg1_start[0] = self.north_pole_x - self.leg_change_x
            self.leg1_start[1] = self.helike_center_y + self.helike_rad
            self.leg1_end[0] = self.north_pole_x
            self.leg1_end[1] = self.leg1_start[1] + self.leg_change_y
            self.leg2_start[0] = self.leg1_start[0] + 2*self.leg_change_x
            self.leg2_start[1] = self.leg1_start[1]
            self.leg2_end[0] = self.north_pole_x
            self.leg2_end[1] = self.leg1_end[1]

            self.body_start[0] = self.leg1_end[0]
            self.body_start[1] = self.leg1_end[1]
            self.body_end[0] = self.leg1_end[0]
            self.body_end[1] = self.leg2_end[1] + self.body_change

            self.arm_start[0] = self.north_pole_x
            self.arm_start[1] = self.leg1_end[1] + self.arm_height
            self.arm_end[0] = self.north_pole_x + self.arm_len
            self.arm_end[1] = self.leg1_end[1] + self.arm_height

            self.head_center_x = self.body_end[0]
            self.head_center_y = self.body_end[1] + self.head_rad

            self.line_x = self.helike_center_x
            self.line_y = self.helike_center_y

            self.line_x2 = self.helike_center_x + (math.cos(math.radians(self.line_angle)) * self.helike_rad)
            self.line_y2 = self.helike_center_y + (math.sin(math.radians(self.line_angle)) * self.helike_rad)

            # find angle
            self.angle_from_sin = math.degrees(math.asin((self.projectile_y-self.helike_center_y)/(((self.projectile_x-self.helike_center_x)**2)+((self.projectile_y-self.helike_center_y)**2))**(1/2)))
            self.angle_from_cos = math.degrees(math.acos((self.projectile_x-self.helike_center_x)/(((self.projectile_x-self.helike_center_x)**2)+((self.projectile_y-self.helike_center_y)**2))**(1/2)))


            if self.angle_from_cos > 0 and self.angle_from_cos < 180:
                self.line_angle = self.angle_from_cos
            if 180-self.angle_from_sin < 180 and 180-self.angle_from_cos+180 > 180 and self.angle_from_cos > 135 and 180-self.angle_from_sin < 180 < 210:
                self.line_angle = 180-self.angle_from_sin
            if 180-self.angle_from_sin > 180 and 180-self.angle_from_cos+180 > 180 and 180-self.angle_from_cos+180 < 340:
                self.line_angle = 180-self.angle_from_cos+180
            if 180-self.angle_from_cos+180 > 320:
                self.line_angle = self.angle_from_sin + 360

            self.tangent_angle = self.line_angle + 90

            self.tangent_x = self.line_x2  + 25 * math.cos(math.radians(self.tangent_angle))
            self.tangent_y = self.line_y2  + 25 * math.sin(math.radians(self.tangent_angle))
            self.tangent_x2 = self.line_x2  - 25 * math.cos(math.radians(self.tangent_angle))
            self.tangent_y2 = self.line_y2  - 25 * math.sin(math.radians(self.tangent_angle))

            # gravity
            self.projectile_distance_from_center = ((self.projectile_x-self.helike_center_x)**2+(self.projectile_y-self.helike_center_y)**2)**(1/2)

            self.force_on_projectile = self.gravity_constant/(((self.projectile_distance_from_center**2)))

            if self.line_angle > 0 and self.line_angle < 180:
                self.projectile_acc_y = (-self.force_on_projectile * math.sin(math.radians(self.line_angle)))
            else:
                self.projectile_acc_y = (-self.force_on_projectile * math.sin(math.radians(self.line_angle)))

            if self.line_angle > 90 and self.line_angle < 270:
                self.projectile_acc_x = (-self.force_on_projectile * math.cos(math.radians(self.line_angle)))
            else:
                self.projectile_acc_x = (-self.force_on_projectile * math.cos(math.radians(self.line_angle)))

            self.projectile_y2 = self.projectile_y + self.projectile_velocity_y*self.time + (1/2*self.projectile_acc_y)*(self.time**2)
            self.projectile_x2 = self.projectile_x + self.projectile_velocity_x*self.time + (1/2*self.projectile_acc_x)*(self.time**2)

            self.projectile_velocity_y = self.projectile_velocity_y + self.projectile_acc_y * self.time
            self.projectile_velocity_x = self.projectile_velocity_x + self.projectile_acc_x * self.time

            self.angle_from_sin = math.degrees(math.asin((self.projectile_y2-self.projectile_y)/(((self.projectile_x2-self.projectile_x)**2)+((self.projectile_y2-self.projectile_y)**2))**(1/2)))
            self.angle_from_cos = math.degrees(math.acos((self.projectile_x2-self.projectile_x)/(((self.projectile_x2-self.projectile_x)**2)+((self.projectile_y2-self.projectile_y)**2))**(1/2)))

            if self.angle_from_cos > 0 and self.angle_from_cos < 180:
                self.projectile_angle  = self.angle_from_cos
            if 180-self.angle_from_sin < 180 and 180-self.angle_from_cos+180 > 180 and self.angle_from_cos > 135 and 180-self.angle_from_sin < 180 < 210:
                self.projectile_angle  = 180-self.angle_from_sin
            if 180-self.angle_from_sin > 180 and 180-self.angle_from_cos+180 > 180 and 180-self.angle_from_cos+180 < 340:
                self.projectile_angle  = 180-self.angle_from_cos+180
            if 180-self.angle_from_cos+180 > 320:
                self.projectile_angle  = self.angle_from_sin + 360


            self.projectile_velocity = (((self.projectile_x2-self.projectile_x)**2+(self.projectile_y2-self.projectile_y)**2)**(1/2))/self.time
            
            self.projectile_distance_from_center  = ((self.projectile_x2-self.helike_center_x)**2+(self.projectile_y2-self.helike_center_y)**2)**(1/2)

            if self.projectile_distance_from_center >= self.helike_rad + self.projectile_rad:
                self.projectile_y = self.projectile_y2
                self.projectile_x = self.projectile_x2

            if self.projectile_distance_from_center < self.helike_rad + self.projectile_rad:
                self.projectile_angle = self.tangent_angle-self.projectile_angle+self.tangent_angle
                self.projectile_velocity_y = self.projectile_velocity * math.sin(math.radians(self.projectile_angle))
                self.projectile_velocity_x = self.projectile_velocity * math.cos(math.radians(self.projectile_angle))
                
                self.projectile_x = self.projectile_x2 + ((self.projectile_x2-self.projectile_x)**2+(self.projectile_y2-self.projectile_y)**2)**(1/2)*math.cos(math.radians(self.projectile_angle))
                self.projectile_y = self.projectile_y2 + (((self.projectile_x2-self.projectile_x)**2+(self.projectile_y2-self.projectile_y)**2)**(1/2))*math.sin(math.radians(self.projectile_angle))
                  


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
