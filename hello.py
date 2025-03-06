
# Setup the GPIO pin (GP10 or GP11) where your LED is connected
# led = Pin(10, Pin.OUT) 

#  # Change 10 to 11 if using GPIO 11 for LED 2

# while True:
#     led.value(1)  # Turn the LED on
#     time.sleep(1)  # Wait for 1 second
#     led.value(0)  # Turn the LED off
#     time.sleep(1)  # Wait for 1 second

print("Hello Pico World")

# simplist Blinky program
# from machine import Pin
# import time
# pin = PIN("LED", Pin.Out)

# while True:
#     pin.value(1)
#     time.sleep(1)
#     pin.value(0)
#     time.sleep(1)

from machine import Pin
import time



# Define the LEDs
led1 = Pin(10, Pin.OUT)
led2 = Pin(11, Pin.OUT)
led3 = Pin(14, Pin.OUT)
led4 = Pin(15, Pin.OUT, value=0)  # Explicitly set as output with initial low value
from utime import sleep

pin = Pin("LED", Pin.OUT)

print("LED starts flashing...")
while True:
    led1.value(1)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    time.sleep(0.5)

    led1.value(0)
    led2.value(1)
    led3.value(0)
    led4.value(0)
    time.sleep(0.5)

    led1.value(0)
    led2.value(0)
    led3.value(1)
    led4.value(0)
    time.sleep(0.5)

    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(1)  
    time.sleep(0.5)


# def new_func():
#     print("Hello Pico World")

# # simplist Blinky program
#     from ctypes.wintypes import PINT
#     from machine import Pin
#     import time
#     pin = PINT("LED", Pin.Out)

#     while True:
#         pin.value(1)
#         time.sleep(1)
#         pin.value(0)
#         time.sleep(1)
    try:
        pin.toggle()
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")

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
