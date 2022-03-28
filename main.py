# Python program to illustrate the concept
# of threading
# importing the threading module
import threading
import time

def print_cube(num):
    """
    function to print cube of given num
    """
    print("Cube: {}".format(num * num * num))


def print_square(num):
    """
    function to print square of given num
    """
    print("Square: {}".format(num * num))


def start_clock(a):
    while(1):
        time.sleep(a)
        print("timer done!")


def test():
    return 1,2

if __name__ == "__main__":

    print(test()==(1,3))