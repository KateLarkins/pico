from machine import Pin, PWM
import time

# Set up the GPIO pins as output for controlling the buzzer
buzzer_pin_10 = Pin(10, Pin.OUT)  # GP10 connected to buzzer
buzzer_pin_11 = Pin(11, Pin.OUT)  # GP11 (additional current source)
buzzer_pin_12 = Pin(12, Pin.OUT)  # GP12 (additional current source)

# Set up PWM on each of the pins
pwm_10 = PWM(buzzer_pin_10)
pwm_11 = PWM(buzzer_pin_11)
pwm_12 = PWM(buzzer_pin_12)

# Set frequency of PWM (in Hz) – adjust to control pitch of the buzzer
pwm_10.freq(1000)  # Frequency of 1kHz is typical for buzzer tones
pwm_11.freq(1000)
pwm_12.freq(1000)

# Initial duty cycle (controls intensity, max value 65535)
pwm_10.duty_u16(32767)  # 50% duty cycle to avoid overdriving buzzer
pwm_11.duty_u16(32767)
pwm_12.duty_u16(32767)

# Function to pulse the buzzer in cycles
def pulse_buzzer(cycles):
    for _ in range(cycles):
        pwm_10.duty_u16(32767)  # Set a 50% duty cycle
        pwm_11.duty_u16(32767)
        pwm_12.duty_u16(32767)
        time.sleep(0.5)  # Buzz for half a second
        pwm_10.duty_u16(0)  # Turn off the buzzer
        pwm_11.duty_u16(0)
        pwm_12.duty_u16(0)
        time.sleep(0.5)  # Wait for half a second

# Function to stop the buzzer completely
def stop_buzzer():
    pwm_10.duty_u16(0)  # Turn off the buzzer completely
    pwm_11.duty_u16(0)
    pwm_12.duty_u16(0)

# Example usage: Pulse the buzzer for 5 cycles
pulse_buzzer(5)

# Stop buzzer after the pulses
stop_buzzer()

# Optionally, keep the buzzer off and wait
time.sleep(1)  # Wait for a second

# If you need to turn it on again, you can call pulse_buzzer or start PWM with a specific duty cycle
# For example, you can restart buzzing:
pwm_10.duty_u16(32767)  # Set the buzzer to pulse again at 50% intensity
pwm_11.duty_u16(32767)
pwm_12.duty_u16(32767)
time.sleep(5)  # Let it buzz for 5 seconds
stop_buzzer()  # Ensure the buzzer is stopped
