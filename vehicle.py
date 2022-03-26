import random

class Vehicle:


    def __init__(self):
        self.direction = None
        self.position_x=None
        self.position_y=None

        if random.randint(0, 1) == 0:  # 50/50 chance of either type being generated
            self.type = 'A'
        else:
            self.type = 'H'

    def set_direction(self,_direction): #stores the direction of the vehicle
        self.direction=_direction

    def set_position(self,x,y):
        self.position_y = y
        self.position_x = x




