from machine import Pin
import time


switch = Pin(4,Pin.IN, Pin.PULL_UP)
led = Pin(2,Pin.OUT)
counter = 0

while(counter < 10):
    switchState = switch.value()
 #   print(switchState)

    if(switchState == 0):
        print("switch is pressed")
        led.on()
        counter = counter + 1
        time.sleep(1)
    else:
        print("switch not pressed")
        led.off()
        counter = counter + 1
        time.sleep(1)

   #     time.sleep(0.1)
        
   # if(switchState == 1):
   #     print("switch not pressed")
    #    led.off()
     #   time.sleep(0.1)

