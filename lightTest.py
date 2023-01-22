from machine import Pin
import time
obled = Pin("LED", Pin.OUT)
led = Pin(13, Pin.OUT)


obled.on() 
led.off()


while True:
    time.sleep(.5)
    obled.off()
    led.on()
    time.sleep(.5)
    obled.on() 
    led.off()
    
    