import badger2040
from picographics import PicoGraphics, DISPLAY_INKY_PACK
import time


badger = badger2040.Badger2040()
display = PicoGraphics(display=DISPLAY_INKY_PACK)

w, h = display.get_bounds()

def get_co2_reading():
    snark = ["ok", "fine", "bad"]
    
    return 400, snark[1]

while True:
    display.set_pen(15)
    display.clear()

    display.set_pen(0)
    
    display.set_font("bitmap8")
    
    # Heading
    display.line(0, 2, w, 2, 4)
    display.text("$ badgerstation", 0, 6, scale=3)
    display.line(0, 34, w, 34, 4)
    
    # CO_2
    display.text("CO", 0, 44, scale = 2)
    display.text("2", 20, 52, scale = 1)
    co2, snark = get_co2_reading()
    display.text(f"is {co2} ppm (which is {snark})", 32, 44, scale = 2)
    
    # Temperature
    display.text(f"Temperature is {18}°C", 0, 76, scale = 2)
    # RH
    display.text(f"Relative humidity is {80}%", 0, 96, scale = 2)
    
    # End
    display.line(0, 124, w, 124, 4)

    display.update()
    
    time.sleep(15)
