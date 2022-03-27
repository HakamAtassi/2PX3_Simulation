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


if __name__ == "__main__":
    # creating thread
    t3=threading.Thread(target=start_clock,args=(4,))
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    # starting thread 1
    t3.start()

    t1.start()
    # starting thread 2
    t2.start()



    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    t3.join()


    # both threads completely executed
    print("Done!")