import time
import board
import digitalio

print("hello blinky!")

led1 = digitalio.DigitalInOut(board.D17)
led1.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.D27)
led2.direction = digitalio.Direction.OUTPUT

led3 = digitalio.DigitalInOut(board.D22)
led3.direction = digitalio.Direction.OUTPUT

led4 = digitalio.DigitalInOut(board.D4)
led4.direction = digitalio.Direction.OUTPUT

leds = [led1,led2,led3,led4]

[setattr(led, 'value', True) for led in leds]

for led in leds:
    led.value = False
    time.sleep(1)


