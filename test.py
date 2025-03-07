from machine import Pin, PWM
import time

# Set up the GPIO 12 pin as output for the buzzer
buzzer = Pin(12, Pin.OUT)

# Set up PWM on the buzzer pin
pwm = PWM(buzzer)
pwm.freq(1000)  # Set frequency (in Hz)

# Set a duty cycle for the PWM (from 0 to 1023, 1023 is full power)
pwm.duty(512)  # Adjust this value to control the buzz strength

time.sleep(5)  # Let it buzz for 5 seconds

# Stop the PWM
pwm.duty(0)  # Stop the buzzer
