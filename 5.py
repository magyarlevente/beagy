from sense_hat import SenseHat
from random import randint
import random
from time import sleep

sense = SenseHat() 

def random_colour():
    random_red = randint(0, 255)  
    random_green = randint(0, 255) 
    random_blue = randint(0, 255) 
    return (random_red, random_green, random_blue)

sense.show_letter("L", random_colour())
sleep(1)
sense.show_letter("e", random_colour())
sleep(1)
sense.show_letter("v", random_colour())
sleep(1)
sense.show_letter("i", random_colour())