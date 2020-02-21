#!/usr/bin/env python3

import arcade,math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):

    helike_scale_factor = 0
    helike_scale_up = False
    helike_scale_down = False
    helike_move_x = 0
    helike_move_y = 0
    helike_center_x = 400
    helike_center_y = 500
    helike_rad = 200
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
    angle_up = False
    angle_down = False

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        # Set up your game here
        pass

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()

        arcade.draw_circle_filled(self.helike_center_x, self.helike_center_y, self.helike_rad, arcade.color.GREEN)
        arcade.draw_line(self.north_x,self.north_y,self.north_x,self.north_y+50, arcade.color.RED, 5)
        arcade.draw_line(self.east_x, self.east_y,self.east_x+50,self.east_y,arcade.color.RED,5)
        arcade.draw_line(self.south_x, self.south_y,self.south_x,self.south_y-50,arcade.color.RED,5)
        arcade.draw_line(self.west_x,self.west_y,self.west_x-50,self.west_y,arcade.color.RED,5)
        #arcade.draw_line(self.line_x,self.line_y,self.line_x2,self.line_y2, arcade.color.RED,5)
        
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

        self.helike_center_x = self.helike_center_x - (self.line_x2 - 400)
        self.helike_center_y = self.helike_center_y - (self.line_y2 - 300) 
        
        if self.helike_scale_up == True:
            if self.helike_rad < 3000:
                self.helike_rad = self.helike_rad * 1.01
        elif self.helike_scale_down == True:
            if self.helike_rad > 100:
                self.helike_rad = self.helike_rad * 0.99

        #self.helike_center_y = 500 - self.helike_rad - 200


        self.line_x = self.helike_center_x
        self.line_y = self.helike_center_y

        if self.angle_up == True:
            self.line_angle += 1
        if self.angle_down == True:
            self.line_angle -= 1

        self.line_x2 = self.helike_center_x + (math.cos(math.radians(self.line_angle)) * self.helike_rad)
        self.line_y2 = self.helike_center_y + (math.sin(math.radians(self.line_angle)) * self.helike_rad)
        

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
