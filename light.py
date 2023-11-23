import badger2040
import time
import math

badger = badger2040.Badger2040()

brightness = 0.0
brightness_delta = 0.05
delay = 0.01


while True:
    # brightness ranges from [0 - 255], both inclusive.
    badger.led(int(128 * math.sin(brightness) + 127))
    
    brightness += brightness_delta
    time.sleep(delay)