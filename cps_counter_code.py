from machine import Pin
import time

switch = Pin(4, Pin.IN, Pin.PULL_UP)
led = Pin(2, Pin.OUT)

clicks = 0
test_time = 5   # seconds

start_time = time.time()

last_state = 1   # button not pressed (PULL_UP)

print("CPS Test Started... Click the button!")

while time.time() - start_time < test_time:

    current_state = switch.value()

    # Detect new press (HIGH -> LOW)
    if last_state == 1 and current_state == 0:
        clicks += 1
        led.on()
        print("Click:", clicks)

    if current_state == 1:
        led.off()

    last_state = current_state

    time.sleep(0.01)   # small delay (10ms)

# Calculate CPS
cps = clicks / test_time

print("Test Finished")
print("Total Clicks:", clicks)
print("CPS:", cps)