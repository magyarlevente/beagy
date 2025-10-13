from sense_hat import SenseHat
from time import sleep
from math import sqrt

sense = SenseHat()
sense.clear()

B = [0, 0, 0]
G = [100, 100, 100]
Y = [255, 255, 0]
P = [150, 75, 0]

cat1 = [
    B, B, B, G, G, B, B, B,
    B, B, G, Y, Y, G, B, B,
    B, G, G, G, G, G, G, B,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    B, G, B, G, G, B, G, B,
    P, B, P, B, B, P, B, P,
    B, B, B, B, B, B, B, B
]

cat2 = [
    B, B, B, G, G, B, B, B,
    B, B, G, Y, Y, G, B, B,
    B, G, G, G, G, G, G, B,
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    B, G, B, G, G, B, G, B,
    B, P, B, P, P, B, P, B,
    B, B, B, B, B, B, B, B
]

def animate_cat():
    for _ in range(6):
        sense.set_pixels(cat1)
        sleep(0.5)
        sense.set_pixels(cat2)
        sleep(0.5)
    sense.clear()

def detect_movement(threshold=1.3):
    accel = sense.get_accelerometer_raw()
    x = accel['x']
    y = accel['y']
    z = accel['z']
    F = sqrt(x**2 + y**2 + z**2)
    return F > threshold

print("Walking Cat – Move the Sense HAT to make the cat walk!")

try:
    while True:
        if detect_movement():
            animate_cat()
        sleep(0.2)
except KeyboardInterrupt:
    sense.clear()
    print("\nProgram stopped.")
