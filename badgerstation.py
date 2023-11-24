import badger2040
from picographics import PicoGraphics, DISPLAY_INKY_PACK
from pimoroni_i2c import PimoroniI2C
from scd30 import SCD30
import time


badger = badger2040.Badger2040()
display = PicoGraphics(display=DISPLAY_INKY_PACK)
i2c = PimoroniI2C(4, 5)
scd30 = SCD30(i2c, 0x61)
w, h = display.get_bounds()

while True:
    while scd30.get_status_ready() != 1:
        time.sleep(0.2)

    # Sensor data
    co2, t, rh = scd30.read_measurement()
    co2_display = f"{co2:.0f}"
    co2_snark = "fine" if co2 <= 1000 else "bad"
    t_dispaly = f"{t:.0f}"
    rh_display = f"{rh:.2f}"

    display.set_pen(15)
    display.clear()

    display.set_pen(0)

    display.set_font("bitmap8")

    # Heading
    display.line(0, 2, w, 2, 4)
    display.text("./badgerstation.py", 0, 6, scale=3)
    display.line(0, 34, w, 34, 4)

    # CO_2
    display.text("CO", 0, 44, scale=2)
    display.text("2", 20, 52, scale=1)
    display.text(f"is {co2_display} ppm (which is {co2_snark})", 32, 44, scale=2)

    # Temperature
    display.text(f"Temperature is {t_dispaly}°C", 0, 76, scale=2)
    # RH
    display.text(f"Relative humidity is {rh_display}%", 0, 96, scale=2)

    # End
    display.line(0, 124, w, 124, 4)

    display.update()

    time.sleep(30)
