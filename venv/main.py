import machine as m
import time
pin = m.Pin(5,m.Pin.OUT)


def blink_led():

    for i in range(0,100):
        pin.value(1)
        time.sleep_ms(500)
        pin.value(0)
        time.sleep_ms(500)



if __name__=="__main__":

    blink_led()

