import RPi.GPIO as GPIO
import time

TRIG = 23
ECHO = 24
BUZZER = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)

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
        if d < 20:
            GPIO.output(BUZZER, True)
        else:
            GPIO.output(BUZZER, False)
        time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
