import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define GPIO pins
TRIG = 17
ECHO = 27

# Set up GPIO pins
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def distance():
    # Send a 10µs pulse to the TRIG pin
    GPIO.output(TRIG, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)
    
    # Wait for the ECHO pin to go HIGH and then LOW
    while GPIO.input(ECHO) == GPIO.LOW:
        pulse_start = time.time()
    while GPIO.input(ECHO) == GPIO.HIGH:
        pulse_end = time.time()
    
    # Calculate pulse length and distance
    pulse_duration = pulse_end - pulse_start
    distance_cm = pulse_duration * 34300 / 2
    return distance_cm

try:
    while True:
        dist = distance()
        print(f"Distance: {dist:.2f} cm")
        time.sleep(1)
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
