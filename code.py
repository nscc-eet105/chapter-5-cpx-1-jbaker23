# My name is Jacob Baker and this is Ch 5 CPX 1 and I am completing this on June 25

from adafruit_circuitplayground import cp
import time

def scale(value):
    index = int(value/306 * 10)
    return index

def pixel_light():
    for i in range(10):
        cp.pixels[i] = (255, 0, 0)

def black():
    for i in range(10):
        cp.pixels[i] = (0, 0, 0)
def main():
    while True:
        light = cp.light
        print((light,))
        time.sleep(.5)
        num_lights = scale(light)
        for i in range(0, 10, 1):
            if i < num_lights:
                pixel_light()
            else:
                black()

main()
