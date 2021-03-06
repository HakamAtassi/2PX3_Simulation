import random


class Vehicle:

    def __init__(self):
        self.direction = None
        self.position_x = None
        self.position_y = None

        if random.randint(0, 1) == 0:
            self.type = 'A'  # Autonomous Vehicle
        else:
            self.type = 'H'  # Human Driven Vehicle

        self.in_intersection_square = False
        self.time_in_intersection = 0

    def set_direction(self, _direction):  # stores the direction of the vehicle
        self.direction = _direction

    def set_position(self, x, y):
        self.position_y = y
        self.position_x = x

    def take_step(self):

        if (self.direction == "Up"):
            self.position_y = self.position_y - 1
            if self.position_y < 0:
                raise Exception
        elif (self.direction == "Down"):
            self.position_y = self.position_y + 1
            if self.position_y > 14:
                raise Exception
        elif (self.direction == "Right"):
            self.position_x = self.position_x + 1
            if self.position_x > 14:
                raise Exception
        elif (self.direction == "Left"):
            self.position_x = self.position_x - 1
            if self.position_x < 0:
                raise Exception

    def is_at_intersection(self):  # is the car at the traffic light?
        if (self.direction == "Up"):  ##important because cars should still take a step even if light is red
            if (self.position_y == 9):
                return True
        elif (self.direction == "Down"):
            if (self.position_y == 5):
                return True
        elif (self.direction == "Right"):
            if (self.position_x == 5):
                return True
        elif (self.direction == "Left"):
            if (self.position_x == 9):
                return True
        return False

    def current_position(self):  ##helper function for can move
        ##same format as front position for easy comparision
        return self.position_y, self.position_x

    def in_square(self):

        if self.current_position() == (6, 6) or self.current_position() == (7, 6) or self.current_position() == (8, 6):
            self.in_intersection_square = True
            return True
        elif self.current_position() == (6, 7) or self.current_position() == (7, 7) or self.current_position() == (
        8, 7):
            self.in_intersection_square = True
            return True
        elif self.current_position() == (6, 8) or self.current_position() == (7, 8) or self.current_position() == (
        8, 8):
            self.in_intersection_square = True
            return True

        else:
            self.in_intersection_square = False
            return False

    def front_position(self):
        if (self.direction == "Up"):
            return self.position_y - 1, self.position_x
        elif (self.direction == "Down"):
            return self.position_y + 1, self.position_x
        elif (self.direction == "Right"):
            return self.position_y, self.position_x + 1
        elif (self.direction == "Left"):
            return self.position_y, self.position_x - 1
