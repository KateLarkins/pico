from machine import Pin, PWM
import time

# Set the GPIO pins for controlling the MOSFETs (connected to the Gates)
gate_pin_1 = PWM(Pin(3))  # Use PWM on GPIO 10 (GP3) for first buzzer
gate_pin_1.freq(1000)  # Set frequency to 1kHz (adjust as needed)
gate_pin_1.duty_u16(0)  # Start with the first buzzer OFF

gate_pin_2 = PWM(Pin(4))  # Use PWM on GPIO 11 (GP4) for second buzzer
gate_pin_2.freq(1000)  # Set frequency to 1kHz (adjust as needed)
gate_pin_2.duty_u16(0)  # Start with the second buzzer OFF

gate_pin_3 = PWM(Pin(5))  # Use PWM on GPIO 12 (GP5) for third buzzer
gate_pin_3.freq(1000)  # Set frequency to 1kHz (adjust as needed)
gate_pin_3.duty_u16(0)  # Start with the third buzzer OFF

# Function to pulse the buzzers in the pattern "DUN DUN DUN" followed by "Another One Bites the Dust"
def pulse_buzzers():
    print("Buzzer Loop Started... Press Ctrl+C to stop.")
    
    while True:  # Infinite loop
        # First "DUN" for buzzer 3 (GP3) - Slower
        print("Buzzer 3 (GP12) DUN")
        gate_pin_3.duty_u16(32768)  # 50% duty cycle for 0.5 seconds
        time.sleep(0.5)
        gate_pin_3.duty_u16(0)  # Turn off GP12

        # Second "DUN" for buzzer 2 (GP4) - Slower
        print("Buzzer 2 (GP11) DUN")
        gate_pin_2.duty_u16(32768)  # 50% duty cycle for 0.5 seconds
        time.sleep(0.5)
        gate_pin_2.duty_u16(0)  # Turn off GP11

        # Third "DUN" for buzzer 1 (GP5) - Slower
        print("Buzzer 1 (GP10) DUN")
        gate_pin_1.duty_u16(32768)  # 50% duty cycle for 0.5 seconds
        time.sleep(0.5)
        gate_pin_1.duty_u16(0)  # Turn off GP10

        # Shorter pause before the next part
        time.sleep(0.3)  # Shorter pause between "DUN DUN DUN" and "Another One Bites the Dust"
        
        # Start pattern: "Another One" for faster buzzing on buzzer 1 (GP10) only
        # First "Another One" for buzzer 1 (GP3)
        print("Buzzer 1 (GP10) Another One")
        gate_pin_1.duty_u16(32768)  # 50% duty cycle for 0.2 seconds
        time.sleep(0.2)
        gate_pin_1.duty_u16(0)  # Turn off GP10

        # Second "Another One" for buzzer 1 (GP3)
        print("Buzzer 1 (GP10) Another One")
        gate_pin_1.duty_u16(32768)  # 50% duty cycle for 0.2 seconds
        time.sleep(0.2)
        gate_pin_1.duty_u16(0)  # Turn off GP10

        # Third "Another One" for buzzer 1 (GP3)
        print("Buzzer 1 (GP10) Another One")
        gate_pin_1.duty_u16(32768)  # 50% duty cycle for 0.2 seconds
        time.sleep(0.2)
        gate_pin_1.duty_u16(0)  # Turn off GP10
        

        # Start pattern: "Bites" for buzzer 2 (GP4)
        # First "Bites" for buzzer 2 (GP11)
        print("Buzzer 2 (GP11) Bites")
        gate_pin_2.duty_u16(32768)  # 50% duty cycle for 0.1 seconds
        time.sleep(0.1)
        gate_pin_2.duty_u16(0)  # Turn off GP11

        # Second "Bites" for buzzer 2 (GP4)
        print("Buzzer 2 (GP11) Bites")
        gate_pin_2.duty_u16(32768)  # 50% duty cycle for 0.1 seconds
        time.sleep(0.1)
        gate_pin_2.duty_u16(0)  # Turn off GP11
         # Third  "Bites" for buzzer 2 (GP4)
        print("Buzzer 2 (GP11) Bites")
        gate_pin_2.duty_u16(32768)  # 50% duty cycle for 0.1 seconds
        time.sleep(0.1)
        gate_pin_2.duty_u16(0)  # Turn off GP11
             # Third  "Bites" for buzzer 2 (GP4)
        print("Buzzer 2 (GP11) Bites")
        gate_pin_2.duty_u16(32768)  # 50% duty cycle for 0.1 seconds
        time.sleep(0.1)
        gate_pin_2.duty_u16(0)  # Turn off GP11

        # Start pattern: "The Dust" for buzzer 3 (GP5)
        # First "The" for buzzer 3 (GP12)
        print("Buzzer 3 (GP12) The")
        gate_pin_3.duty_u16(32768)  # 50% duty cycle for 0.1 seconds
        time.sleep(0.1)
        gate_pin_3.duty_u16(0)  # Turn off GP12

        # Second "Dust" for buzzer 3 (GP5)
        print("Buzzer 3 (GP12) Dust")
        gate_pin_3.duty_u16(32768)  # 50% duty cycle for 0.1 seconds
        time.sleep(0.1)
        gate_pin_3.duty_u16(0)  # Turn off GP12
         # 3 "Dust" for buzzer 3 (GP5)
        print("Buzzer 3 (GP12) Dust")
        gate_pin_3.duty_u16(32768)  # 50% duty cycle for 0.1 seconds
        time.sleep(0.1)
        gate_pin_3.duty_u16(0)  # Turn off GP12

        # Delay before starting the next round
        time.sleep(0.3)  # Small delay to separate repetitions
        time.sleep(0.3)

# Call the function to start pulsing
try:
    pulse_buzzers()
except KeyboardInterrupt:
    print("Stopping buzzers...")
    gate_pin_1.duty_u16(0)  # Ensure buzzer 1 is OFF when stopping
    gate_pin_2.duty_u16(0)  # Ensure buzzer 2 is OFF when stopping
    gate_pin_3.duty_u16(0)  # Ensure buzzer 3 is OFF when stopping
