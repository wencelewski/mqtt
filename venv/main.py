import machine as m
import ssd1306
import time
pin = m.Pin(5,m.Pin.OUT)
i2c = m.I2C(scl=m.Pin(14),sda=m.Pin(12))


def i2c_test():
    print("scaneando i2c..")
    devices = i2c.scan()

    if len(devices) == 0:
        print("Nenhum dispositivo I2C detectado")
    else:
        print("Foram encontrados {} dispositivos".format(len(devices)))

        for device in devices:
            print("Decimal Address: ", device, "| Hexa address:", hex(device))


def blink_led():


    for i in range(0,100):
        pin.value(1)
        time.sleep_ms(500)
        pin.value(0)
        time.sleep_ms(500)



if __name__=="__main__":

#    blink_led()
    #i2c_test()
