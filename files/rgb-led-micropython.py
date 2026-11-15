from machine import Pin, ADC, PWM
from time import sleep

pot = ADC(Pin(26))

red = PWM(Pin(16))
green = PWM(Pin(17))
blue = PWM(Pin(18))

red.freq(1000)
green.freq(1000)
blue.freq(1000)

def set_color(r, g, b):
    red.duty_u16(65535 - r)
    green.duty_u16(65535 - g)
    blue.duty_u16(65535 - b)

set_color(0, 0, 0)

while True:

    value = pot.read_u16()

    position = value * 2 / 65535

    if position <= 1:
        r = int(65535 * (1 - position))
        g = int(65535 * position)
        b = 0

    else:
        r = 0
        g = int(65535 * (2 - position))
        b = int(65535 * (position - 1))

    set_color(r, g, b)

    sleep(0.02)