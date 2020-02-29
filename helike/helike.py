#!/usr/bin/env python3

import arcade,math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    uni_scale_factor = 0
    cycle = 0
    time = 0
    scale_factor = 1
    helike_scale_up = False
    helike_scale_down = False
    helike_center_x = 400
    helike_center_y = 300
    helike_rad = 100
    north_x = 0
    north_y = 0
    east_x = 0
    east_y = 0
    south_x = 0
    south_y = 0
    west_x = 0
    west_y = 0
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

    gravity_constant = 67000#000
    projectile_rad = 10
    projectile_x = helike_center_x + 0
    projectile_y = helike_center_x + projectile_rad + 100
    projectile_y1 = projectile_y
    projectile_rad = 10
    projectile_force_x = 0
    projectile_force_y = 0
    projectile_distance_from_center = 2100
    projectile_distance_from_center1 = 2100
    projectile_displacement = 0
    projectile_velocity = 0
    projectile_angle = 0
    projectile_velocity1 = 0
    projectile_velocity_x = -300
    projectile_velocity_y = -100
    projectile_velocity_x2 = 0
    projectile_velocity_y2 = 0
    projectile_acc_x = 0
    projectile_acc_y = 0

    force_on_projectile = 0

    tangent_angle = 0

    use_sin = False

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        pass

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()

        arcade.draw_circle_filled(self.helike_center_x, self.helike_center_y, self.helike_rad, arcade.color.GREEN)
        #arcade.draw_line(self.north_x,self.north_y,self.north_x,self.north_y+50, arcade.color.RED, 5)
        #arcade.draw_line(self.east_x, self.east_y,self.east_x+50,self.east_y,arcade.color.RED,5)
        #arcade.draw_line(self.south_x, self.south_y,self.south_x,self.south_y-50,arcade.color.RED,5)
        #arcade.draw_line(self.west_x,self.west_y,self.west_x-50,self.west_y,arcade.color.RED,5)
        arcade.draw_line(self.line_x,self.line_y,self.line_x2,self.line_y2, arcade.color.RED,5)
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
            self.helike_scale_up = True
        if key == arcade.key.DOWN:
            self.helike_scale_down = True
        if key == arcade.key.LEFT:
            self.angle_up = True
        if key == arcade.key.RIGHT:
            self.angle_down = True
    

    def on_key_release(self,key,modifiers):
        if key == arcade.key.UP:
            self.helike_scale_up = False
        if key == arcade.key.DOWN:
            self.helike_scale_down = False
        if key == arcade.key.LEFT:
            self.angle_up = False
        if key == arcade.key.RIGHT:
            self.angle_down = False


    def update(self, delta_time):
        
        self.time = 0.013
        
        if self.helike_scale_up == True or self.helike_scale_down == True:
            if self.helike_scale_up == True and self.helike_rad > 100:
                self.projectile_distance_from_center1 += 1
            if self.helike_scale_down == True and self.helike_rad < 3000:
                self.projectile_distance_from_center1 -= 1

        #self.projectile_distance_scale = self.projectile_distance_from_center1

        """
        if self.helike_rad > 100 and self.helike_rad < 3000:

            self.uni_scale_factor = self.projectile_distance_from_center/self.projectile_distance_from_center1
            self.north_pole_scale = self.north_pole_scale * self.uni_scale_factor
            self.projectile_distance_scale = self.projectile_distance_scale / self.uni_scale_factor
            self.projectile_rad = self.projectile_rad * self.uni_scale_factor
            self.helike_rad = self.helike_rad * self.uni_scale_factor

            self.leg1_start[0] = self.leg1_start[0] * self.uni_scale_factor
            self.leg_change_x = self.leg_change_x * self.uni_scale_factor
            self.leg_change_y = self.leg_change_y * self.uni_scale_factor
            self.body_width = self.body_width * self.uni_scale_factor
            self.body_change = self.body_change * self.uni_scale_factor
            self.arm_height = self.arm_height * self.uni_scale_factor
            self.arm_len = self.arm_len * self.uni_scale_factor
            self.head_rad = self.head_rad * self.uni_scale_factor

        """



        if self.angle_up == True:
            self.line_angle += 1
            if self.line_angle == 360:
                self.line_angle = 0
        if self.angle_down == True:
            self.line_angle -= 1
            if self.line_angle == 0:
                self.line_angle = 360


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

        """
        if (round(180-self.angle_from_sin,0) == round(self.angle_from_cos,0) and self.angle_from_cos > 135) or (round(180-self.angle_from_sin,0) == 180-round(self.angle_from_cos,0)+180 and self.angle_from_cos < - 135): #and (180-self.angle_from_sin < 130 and 180-self.angle_from_sin > 130):
            self.use_sin = True
        elif self.use_sin == True and self.angle_from_sin > 0:#180-self.angle_from_sin < 115:
            self.line_angle = self.angle_from_cos
            self.use_sin = False
        elif self.use_sin == True and self.angle_from_sin < 0:#180-self.angle_from_sin > 260:
            self.line_angle = -self.angle_from_cos
            self.use_sin = False
        
        if self.use_sin == False:
            if self.line_angle < 180 and self.line_angle >= -15:
                self.line_angle = self.angle_from_cos # math.degrees(math.acos((self.projectile_x-self.helike_center_x)/(((self.projectile_x-self.helike_center_x)**2)+((self.projectile_y-self.helike_center_y)**2))**(1/2)))
            if self.line_angle < 45 and self.line_angle >= -90:
                self.line_angle = math.degrees(math.asin((self.projectile_y-self.helike_center_y)/(((self.projectile_x-self.helike_center_x)**2)+((self.projectile_y-self.helike_center_y)**2))**(1/2)))
            if self.line_angle < -45 and self.line_angle >= -180:
                self.line_angle = -math.degrees(math.acos((self.projectile_x-self.helike_center_x)/(((self.projectile_x-self.helike_center_x)**2)+((self.projectile_y-self.helike_center_y)**2))**(1/2)))
            #if self.angle_from_cos > 135 and self.angle_from_sin < -135:
                #self.line_angle = -self.angle_from_sin
        else:
            self.line_angle = 180 -self.angle_from_sin
        """

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

        self.force_on_projectile = self.gravity_constant/(((self.projectile_distance_from_center)))

        if self.line_angle > 0 and self.line_angle < 180:
            self.projectile_acc_y = -self.force_on_projectile * math.sin(math.radians(self.line_angle))
        else:
            self.projectile_acc_y = -self.force_on_projectile * math.sin(math.radians(self.line_angle))

        if self.line_angle > 90 and self.line_angle < 270:
            self.projectile_acc_x = -self.force_on_projectile * math.cos(math.radians(self.line_angle))
        else:
            self.projectile_acc_x = -self.force_on_projectile * math.cos(math.radians(self.line_angle))

        self.projectile_y2 = self.projectile_y + self.projectile_velocity_y*self.time + (1/2*self.projectile_acc_y)*(self.time**2)
        self.projectile_x2 = self.projectile_x + self.projectile_velocity_x*self.time + (1/2*self.projectile_acc_x)*(self.time**2)

        self.projectile_velocity_y = self.projectile_velocity_y + self.projectile_acc_y * self.time
        self.projectile_velocity_x = self.projectile_velocity_x + self.projectile_acc_x * self.time

        self.projectile_angle = -math.degrees(math.asin((self.projectile_y2-self.projectile_y)/((self.projectile_x2-self.projectile_x)**2+(self.projectile_y2-self.projectile_y)**2)**(1/2)))

        self.projectile_velocity = (((self.projectile_x2-self.projectile_x)**2+(self.projectile_y2-self.projectile_y)**2)**(1/2))/self.time
        
        self.projectile_y = self.projectile_y2
        self.projectile_x = self.projectile_x2
        
        self.projectile_distance_from_center = ((self.projectile_x-self.helike_center_x)**2+(self.projectile_y-self.helike_center_y)**2)**(1/2)


        if self.projectile_distance_from_center <= self.helike_rad + self.projectile_rad:
            self.projectile_angle = -self.projectile_angle
            self.projectile_velocity_y = self.projectile_velocity * math.sin(math.radians(self.projectile_angle))
            self.projectile_velocity_x = self.projectile_velocity * math.cos(math.radians(self.projectile_angle))

        #print(self.projectile_x,self.projectile_y)

        self.north_x = self.helike_center_x
        self.north_y = self.helike_center_y + self.helike_rad
        self.east_x = self.helike_center_x + self.helike_rad
        self.east_y = self.helike_center_y
        self.south_x = self.helike_center_x
        self.south_y = self.helike_center_y - self.helike_rad
        self.west_x = self.helike_center_x - self.helike_rad
        self.west_y = self.helike_center_y


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
