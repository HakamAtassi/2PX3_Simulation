import random
from vehicle import Vehicle
import threading
import time
import matplotlib.pyplot as plt
import numpy as np
import math
import numpy
random.seed()

congestion_index = 0.5  # controls congestion/spawn rate


class Colours:
    R = '\033[91m'
    G = '\033[92m'
    END = '\033[0m'
    SD = '\033[96m'
    HD = '\033[93m'

class Intersection:
    ##the intersection will be preresented by a square matrix
    ##vehicles will be denoted by an 'A' for autonomous, 'H' for human. Road is denoted by a space " " char. undrivable road is denoted by an "x".

    ##the intersection will be preresented by a square matrix
    ##r and g indicate the color of the traffic light
    ##on right for each lane
    #   #dwn

    vehicles = []  # stores all the vehicles in traffic

    time_in_intersection_data = []

    intersection_coordinates = [['x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x'],
                                ['x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x'],
                                ['x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x'],
                                ['x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x'],
                                ['x', 'x', 'x', 'x', 'x', 'r', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x'],
                                ['x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'r', 'x', 'x', 'x', 'x'],
                                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                ['x', 'x', 'x', 'x', 'r', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x'],
                                ['x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'r', 'x', 'x', 'x', 'x', 'x'],
                                ['x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x'],
                                ['x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x'],
                                ['x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x'],
                                ['x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x'],
                                ]  #

    def __init__(self):
        self.collisions = 0

    def print_intersection(self):
        for i in range(len(self.intersection_coordinates)):  ##just prints the matrix

            for j in range(len(self.intersection_coordinates[0])):
                if 'r' in self.intersection_coordinates[i][j]:
                    print(Colours.R + self.intersection_coordinates[i][j] + Colours.END, end=' ')
                elif 'g' in self.intersection_coordinates[i][j]:
                    print(Colours.G + self.intersection_coordinates[i][j] + Colours.END, end=' ')
                elif "A" in self.intersection_coordinates[i][j]:
                    print(Colours.SD + self.intersection_coordinates[i][j] + Colours.END, end=' ')
                elif "H" in self.intersection_coordinates[i][j]:
                    print(Colours.HD + self.intersection_coordinates[i][j] + Colours.END, end=' ')
                else:
                    print(self.intersection_coordinates[i][j], end=' ')
            print("\t")
        print("\n<><><><><><><><><><><><><><><>\n")





    def generate_traffic_autonomous(self):  ##a function that only generates self driving cars in "priority lanes
        new_vehicle = Vehicle()
        spawn_chance = random.uniform(0, 1).__round__(2)  # generates random double from 0 to 1
        if spawn_chance >= 0.5:  # this spawn chance depends on time of day. controls congestion
            ##spawn vehicle
            spawn_location = random.randint(0, 1)  # randomizes where the vehicle will spawn

            if spawn_location == 0:
                new_vehicle.type = 'A'
                self.intersection_coordinates[0][7] = new_vehicle.type
                new_vehicle.set_position(7, 0)
                new_vehicle.set_direction("Down")

            if spawn_location == 5:
                new_vehicle.type = 'A'
                self.intersection_coordinates[7][0] = new_vehicle.type
                new_vehicle.set_position(0, 7)
                new_vehicle.set_direction("Right")
        self.vehicles.append(new_vehicle)

    ##Generates letters in place of vehicles. swap with vehicle objects.
    def generate_traffic(self):  # generate traffic for the intersection S
        new_vehicle = Vehicle()
        spawn_chance = random.uniform(0, 1).__round__(2)  # generates random double from 0 to 1
        if spawn_chance >= 0.5:  # this spawn chance depends on time of day. controls congestion
            ##spawn vehicle

            spawn_location = random.randint(0, 5)  # randomizes where the vehicle will spawn
            if spawn_location == 0:
                self.intersection_coordinates[0][6] = new_vehicle.type
                new_vehicle.set_position(6, 0)
                new_vehicle.set_direction("Down")  ##sets direction of vehicle object

            if spawn_location == 1:
                self.intersection_coordinates[6][14] = new_vehicle.type
                new_vehicle.set_position(14, 6)
                new_vehicle.set_direction("Left")
            if spawn_location == 2:
                self.intersection_coordinates[14][8] = new_vehicle.type
                new_vehicle.set_position(8, 14)
                new_vehicle.set_direction("Up")

            if spawn_location == 3:
                self.intersection_coordinates[8][0] = new_vehicle.type
                new_vehicle.set_position(0, 8)
                new_vehicle.set_direction("Right")

            if spawn_location == 4:
                new_vehicle.type = 'A'
                self.intersection_coordinates[0][7] = new_vehicle.type
                new_vehicle.set_position(7, 0)
                new_vehicle.set_direction("Down")

            if spawn_location == 5:
                new_vehicle.type = 'A'
                self.intersection_coordinates[7][0] = new_vehicle.type
                new_vehicle.set_position(0, 7)
                new_vehicle.set_direction("Right")
        self.vehicles.append(new_vehicle)

    def is_empty(self):  ##returns true if there are no cars on the intersection
        for i in range(15):
            for j in range(15):
                if (self.intersection_coordinates[i][j] == 'A' or self.intersection_coordinates[i][
                    j] == 'H'):  ##if an A or H exists in the matrix, its not empty
                    return False
        return True

    def set_lights_red(self, intersection_coordinates):  ##sets all traffic lights off
        self.intersection_coordinates[4][5] = 'r'
        self.intersection_coordinates[5][10] = 'r'
        self.intersection_coordinates[9][4] = 'r'
        self.intersection_coordinates[10][9] = 'r'

    def alternate_traffic_light(self):
        if (self.intersection_coordinates[4][5] == 'g'):
            self.intersection_coordinates[4][5] = 'r'
            self.intersection_coordinates[5][10] = 'g'

        elif (self.intersection_coordinates[5][10] == 'g'):
            self.intersection_coordinates[5][10] = 'r'
            self.intersection_coordinates[10][9] = 'g'


        elif (self.intersection_coordinates[10][9] == 'g'):
            self.intersection_coordinates[10][9] = 'r'
            self.intersection_coordinates[9][4] = 'g'

        elif (self.intersection_coordinates[9][4] == 'g'):
            self.intersection_coordinates[9][4] = 'r'
            self.intersection_coordinates[4][5] = 'g'

        else:
            self.intersection_coordinates[9][4] = 'g'

    def priority_lane_cleared_r(self):  ##check if the "right" priority lane is empty
        counter = 0
        for i in range(6):
            if self.intersection_coordinates[7][i] != ' ':
                counter += 1
        if counter == 0:
            return True
        else:
            return False

    def priority_lane_cleared_l(self):
        counter = 0
        for i in range(6):
            if self.intersection_coordinates[i][7] != ' ':
                counter += 1
        if counter == 0:
            return True
        else:
            return False

    def enable_traffic_lights(self):  # turns on the timed feature of traffic lights
        # if there are no cars and a self-driving car pulls up, let it pass.
        # else, acts on a timer like normal traffic light

        # if (self.is_empty() == True):

        time.sleep(0.05)  ##dont search matrix too often. too energy consuming
        """
        if self.intersection_coordinates[9][4] == 'g':
            while (self.priority_lane_cleared_r() == False):
                time.sleep(0.2)
            print("Traffic light switched\n")
            self.alternate_traffic_light()

        if self.intersection_coordinates[4][5] == 'g':
            while (self.priority_lane_cleared_l() == False):
                time.sleep(0.2)
            print("Traffic light switched\n")
            self.alternate_traffic_light()
            """
        time.sleep(4)
        print("Traffic light switched\n")
        self.alternate_traffic_light()
        self.enable_traffic_lights()

        pass

    def progress_intersection(self):  ##this function takes the next step based on the logic we defined.
        pass

    def get_traffic_signal(self, direction):
        if direction == "Up":
            return self.intersection_coordinates[10][9]
        if direction == "Down":
            return self.intersection_coordinates[4][5]
        if direction == "Right":
            return self.intersection_coordinates[9][4]
        if direction == "Left":
            return self.intersection_coordinates[5][10]

    def clear_intersection(self):  ##is the whole intersection empty?
        for j in range(15):
            for m in range(15):
                if (self.intersection_coordinates[j][m] == 'A' or self.intersection_coordinates[j][m] == 'H'):
                    self.intersection_coordinates[j][m] = ' '

    def vehicle_ahead(self, _vehicle):
        if (self.intersection_coordinates[_vehicle.front_position()[0]][_vehicle.front_position()[1]]) != ' ':
            return True
        return False

    def can_move(self, curr_vehicle):
        """Vehicles enter list based on FIFO. earliest elements move first. if there are no elements in the list that
        occupy the desired location, the next vehicle can move"""
        for i in self.vehicles:
            if (
                    curr_vehicle.front_position() == i.current_position() and i.in_square == False):  ##if there is a vehicle in front and its not in "square
                return False  ##then it cant collide
        return True  ##can collide

    def square_empty(self):  ##are there any cars in the intersection "square"
        for j in range(3):
            if (self.intersection_coordinates[6][6 + j]) != ' ':
                return False
            if (self.intersection_coordinates[7][6 + j]) != ' ':
                return False
            if (self.intersection_coordinates[8][6 + j]) != ' ':
                return False
        return True


    def in_square_test(self):
        insquare=0
        for i in self.vehicles:
            #print(i.in_square())
            if i.in_square()==True:
                insquare+=1

        #print("insquare",insquare)



    def take_step(self):
        try:
            for i in self.vehicles:
                if (self.get_traffic_signal(i.direction) == 'g' or i.is_at_intersection() == False):

                    if (self.can_move(i) == True):
                        try:
                            i.take_step()
                        except:
                            self.vehicles.remove(i)
            self.clear_intersection()

            for i in self.vehicles:
                self.intersection_coordinates[i.position_y][i.position_x] = i.type
        except:
            self.vehicles.pop()
        for i in self.vehicles:
            i.time_in_intersection += 1  ##increment number of steps

    def print_vehicles(self):
        y = []
        x = []
        for i in range(len(self.vehicles)):
            print(self.vehicles[i].time_in_intersection)
            y.append(self.vehicles[i].time_in_intersection)
            x.append(i)
        a = np.array(x)
        b = np.array(y)

        plt.scatter(a, b)
        plt.show()

    def most_congeseted(self):
        ## a function that returns which lane direciton is most congested. just implement but we decided we arent going to actually use it
        ##might be good to talk about during presentation.
        pass


    def count_insquare(self):
        insquare=0
        for i in self.vehicles:
            if i.in_square()==True:
                insquare+=1
        return insquare

    def count_collisions(self):
        collision_chance=random.uniform(0, 1).__round__(2)  # generates random double from 0 to 1
        insquare=0
        #print(self.count_insquare())
        if(collision_chance>1/(numpy.log(self.count_insquare()+1))): #        if(collision_chance>1/numpy.log(insquare+1)):
            self.collisions+=1



        print("collisions: ", self.collisions)


if __name__ == "__main__":

    a = Intersection()
    t1 = threading.Thread(target=a.enable_traffic_lights, args=())

    a.print_intersection()
    t1.start()
    for i in range(100):
        #print("right prio empty: ", a.priority_lane_cleared_r())
        a.generate_traffic()
        #sa.in_square_test()
        # a.generate_traffic_autonomous()
        a.print_intersection()
        time.sleep(0.5)

        a.count_collisions()
        a.take_step()
    a.print_vehicles()

    t1.join()

    """
    a = Intersection()
    a.generate_traffic()
    a.print_intersection()
    print(a.is_empty())
    a.enable_traffic_lights()
    a.print_intersection()
  """
