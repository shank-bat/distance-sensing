import RPi.GPIO as GPIO
import time

TRIG = 23
ECHO = 24
RED = 17
WHITE = 27
GREEN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
for pin in [RED, WHITE, GREEN]:
    GPIO.setup(pin, GPIO.OUT)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO) == 0:
        start = time.time()
    while GPIO.input(ECHO) == 1:
        end = time.time()
    return (end - start) * 17150

try:
    while True:
        d = get_distance()
        GPIO.output(RED, False)
        GPIO.output(WHITE, False)
        GPIO.output(GREEN, False)
        if d < 10:
            GPIO.output(RED, True)
        elif 10 <= d <= 30:
            GPIO.output(WHITE, True)
        elif d > 30:
            GPIO.output(GREEN, True)
        time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
