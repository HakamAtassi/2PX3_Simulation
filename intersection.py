import random
from vehicle import Vehicle

random.seed()

congestion_index = 0.5  # controls congestion/spawn rate


class Intersection:
    ##the intersection will be preresented by a square matrix
    ##vehicles will be denoted by an 'A' for autonomous, 'H' for human. Road is denoted by a space " " char. undrivable road is denoted by an "x".

    ##the intersection will be preresented by a square matrix
    ##r and g indicate the color of the traffic light
    ##on right for each lane
    #   #dwn

    intersection_coordinates = [['x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x'],
                                ['x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x'],
                                ['x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x'],
                                ['x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x'],
                                ['x', 'x', 'x', 'x', 'x', 'r', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x'],
                                ['x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'r', 'x', 'x', 'x', 'x'],
                                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                # dir =>
                                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                ['x', 'x', 'x', 'x', 'r', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x'],
                                ['x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'r', 'x', 'x', 'x', 'x', 'x'],
                                ['x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x'],
                                ['x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x'],
                                ['x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x'],
                                ['x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x'],
                                ]  #

    def print_intersection(self):
        for i in range(len(self.intersection_coordinates)):

            for j in range(len(self.intersection_coordinates[0])):
                print(self.intersection_coordinates[i][j], end=' ')
            print("\t")
        print("\n<><><><><><><><><><><><><><><>\n")

    def initiate_timer(self):  # clock or time based counter. This will be used to measure performance.
        pass

    ##Generates letters in place of vehicles. swap with vehicle objects.
    def generate_traffic(self):  # generate traffic for the intersection S
        new_vehicle = Vehicle()
        spawn_chance = random.uniform(0, 1).__round__(2)  # generates random double from 0 to 1
        if spawn_chance >= 0.5:  # this spawn chance depends on time of day. controls congestion
            ##spawn vehicle

            spawn_location = random.randint(0, 3)  # randomizes where the vehicle will spawn
            if spawn_location == 0:
                self.intersection_coordinates[0][6] = new_vehicle.type
                new_vehicle.set_position(6, 0)
                new_vehicle.set_direction("Down")

            if spawn_location == 1:
                self.intersection_coordinates[6][14] = new_vehicle.type
                new_vehicle.set_position(14, 0)
                new_vehicle.set_direction("Left")
            if spawn_location == 2:
                self.intersection_coordinates[14][6] = new_vehicle.type
                new_vehicle.set_position(0, 14)
                new_vehicle.set_direction("Up")

            if spawn_location == 3:
                self.intersection_coordinates[8][0] = new_vehicle.type
                new_vehicle.set_position(0, 8)
                new_vehicle.set_direction("Right")

    def is_empty(self):  ##returns true if there are no cars on the intersection
        for i in range(15):
            for j in range(15):
                if (self.intersection_coordinates[i][j] == 'A' or self.intersection_coordinates[i][j] == 'H'):
                    return False
        return True

    def set_lights_red(self, intersection_coordinates):  ##sets all traffic lights off
        self.intersection_coordinates[4][5] = 'r'
        self.intersection_coordinates[5][10] = 'r'
        self.intersection_coordinates[9][4] = 'r'
        self.intersection_coordinates[10][9] = 'r'

    def enable_traffic_lights(self):  # turns on the timed feature of traffic lights
        # if there are no cars and a self driving car pulls up, let it pass.
        # else, acts on a timer like normal traffic light

        if (self.is_empty() == True):
            self.set_lights_red(self.intersection_coordinates)

        ## why do we not let human driven cars pass even if its empty?
        ##becuase if the light turns green for a hd car and the car decides to not clear, accidents may occur.

        ##if intersection is clear, turn everything red.
        ## car is generated
        ##pulls up to intersection when empty
        ##self driven?
        ##yes =>make green so car does not stop
        ##no=>wait as normal.
        ##not empty?
        ##use normal timed lights.
        ## what about the self drinving lane? do lights apply to it?
        pass

    def progress_intersection(self):  ##this function takes the next step based on the logic we defined.
        pass

    def most_congeseted(self):
        ## a function that returns which lane direciton is most congested. just implement but we decided we arent going to actually use it
        ##might be good to talk about during presentation.
        pass


if __name__ == "__main__":
    a = Intersection()
    a.generate_traffic()
    a.print_intersection()
    print(a.is_empty())
    a.enable_traffic_lights()
    a.print_intersection()
