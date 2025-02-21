print("Hello Pico World")

# simplist Blinky program
from machine import Pin
import time
pin = PIN("LED", Pin.Out)

while True:
    pin.value(1)
    time.sleep(1)
    pin.value(0)
    time.sleep(1)

# Flash LED
# from machine import Pin
# import time
# pin = PIN(22, Pin.Out)
# while True:
#     pin.value(1)
#     time.sleep(1)
#     pin.value(0)
#     time.sleep(1)

# Easier Version of Blinky using toggle function
# from machine import Pin
# import time
# pin = PIN(22, Pin.Out)
# while True:
    # pin.toggle()
    # time.sleep(1) 

    # See summary pg.36 if it doesn't work

# See how fast a single GPIO line can be used if you have a logic analyzer of oscilloscope
    # from machine import Pin
    # pin = Pin(22, Pin.Out)
    # white True:
        # pin.value(1)
        # pin.value(0)