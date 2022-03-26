import random

random.seed()

congestion_index = 0.5  # controls congestion/spawn rate


class Intersection:
    ##the intersection will be preresented by a square matrix
    ##vehicles will be denoted by an 'A' for autonomous, 'H' for human. Road is denoted by a space " " char. undrivable road is denoted by an "x".

    ##the intersection will be preresented by a square matrix
    ##vehicles will be denoted by an O. Road is denoted by a space " " char. undrivable road is denoted by an "x".
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
                                # 6,14 dir <=
                                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # dir =>
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
        print("\n")

    def initiate_timer(self):  # clock or time based counter. This will be used to measure performance.
        pass

    def generate_traffic(self):  # generate traffic for the intersection S

        if random.randint(0, 1) == 0:
            vehicle = 'A'
        else:
            vehicle = 'H'
        spawn_chance = random.uniform(0, 1).__round__(2)  # generates random double from 0 to 1
        if spawn_chance >= 0.5:  # this spawn chance depends on time of day. controls congestion
            ##spawn vehicle

            spawn_location = random.randint(0, 3)   #randomizes where the vehicle will spawn
            if spawn_location == 0:
                self.intersection_coordinates[0][6] = vehicle;
            if spawn_location == 1:
                self.intersection_coordinates[6][14] = vehicle;
            if spawn_location == 2:
                self.intersection_coordinates[14][6] = vehicle;
            if spawn_location == 3:
                self.intersection_coordinates[8][0] = vehicle;




    def enable_traffic_lights(self):  # turns on the timed feature of traffic lights
        # if there are no cars and a self driving car pulls up, let it pass.
        # else, acts on a timer like normal traffic light
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

    def most_congeseted(
            self):  ## a function that returns which lane direciton is most congested. just implement but we decided we arent going to actually use it
        ##might be good to talk about during presentation.
        pass


if __name__ == "__main__":
    a = Intersection()
    a.print_intersection()
    a.generate_traffic()
    a.print_intersection()
