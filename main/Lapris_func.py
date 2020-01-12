from machine import Pin
import time

def blink_pin(pin):
    for i in range(10):
        led_ = Pin(pin, Pin.OUT)
        led_.on()
        time.sleep(1)
        led_.off()
        time.sleep(1)
        