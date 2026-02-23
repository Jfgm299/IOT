import time
import board
import digitalio

print("hello blinky!")
#1423
led1 = digitalio.DigitalInOut(board.D17)
led1.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.D27)
led2.direction = digitalio.Direction.OUTPUT

led3 = digitalio.DigitalInOut(board.D22)
led3.direction = digitalio.Direction.OUTPUT

led4 = digitalio.DigitalInOut(board.D4)
led4.direction = digitalio.Direction.OUTPUT

while True:

    # S → ...
    led1.value = True
    time.sleep(0.5)
    led1.value = False
    time.sleep(0.5)

    led1.value = True
    time.sleep(0.5)
    led1.value = False
    time.sleep(0.5)

    led1.value = True
    time.sleep(0.5)
    led1.value = False
    time.sleep(1)   # espacio entre letras


    # O → ---
    led1.value = True
    time.sleep(1)
    led1.value = False
    time.sleep(0.5)

    led1.value = True
    time.sleep(1)
    led1.value = False
    time.sleep(0.5)

    led1.value = True
    time.sleep(1)
    led1.value = False
    time.sleep(1)   # espacio entre letras


    # S → ...
    led1.value = True
    time.sleep(0.5)
    led1.value = False
    time.sleep(0.5)

    led1.value = True
    time.sleep(0.5)
    led1.value = False
    time.sleep(0.5)

    led1.value = True
    time.sleep(0.5)
    led1.value = False
    time.sleep(2)
