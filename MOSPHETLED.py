from machine import Pin
import time

# Set the GPIO pin for controlling the MOSFET (connected to the Gate)
gate_pin = Pin(0, Pin.OUT)  # GPIO 13 controls the MOSFET Gate

# Set the built-in LED pin (GPIO 25)
led_pin = Pin(25, Pin.OUT)  # GPIO 25 is connected to the built-in LED

# Function to test the built-in LED using the MOSFET
def test_led():
    print("MOSFET Control Test Started...")

    # Step 1: Turn on the MOSFET (by applying 3.3V to the Gate)
    print("Turning MOSFET ON... Gate to HIGH")
    gate_pin.high()  # Turn the MOSFET ON
    time.sleep(1)  # Give the MOSFET time to turn on

    # Step 2: The built-in LED should be ON now (since MOSFET is on)
    print("MOSFET is ON, built-in LED should be ON now")
    led_pin.high()  # Turn the built-in LED ON
    time.sleep(3)  # Let the LED stay on for 3 seconds

    # Step 3: Turn off the MOSFET (by applying 0V to the Gate)
    print("Turning MOSFET OFF... Gate to LOW")
    gate_pin.low()  # Turn the MOSFET OFF
    led_pin.low()  # Turn the built-in LED OFF
    time.sleep(1)  # Give time for the MOSFET to turn off

    print("Test Complete. MOSFET OFF and built-in LED OFF.")

# Call the test function
test_led()
 