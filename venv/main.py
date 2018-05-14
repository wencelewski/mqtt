import machine as m
import ssd1306
import time
import onewire
from umqtt.simple import MQTTClient
import ubinascii

pin = m.Pin(5,m.Pin.OUT)



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

def sub_cb(topic,msg):
    print((topic,msg))
    if topic == b'ap062/led' and msg == b'1':
        pin.value(1)

    elif topic == b'ap062/led' and msg == b'0':
        pin.value(0)

    elif topic == b'ap062/node_display':
        oled.fill(0)
        oled.show()
        time.sleep(1)
        oled.text(msg, 5, 16)
        oled.show()
    elif topic == b'ap062/temp':
        #read_temp()

if __name__=="__main__":
    SERVER = "test.mosquitto.org"
    CLIENT_ID = ubinascii.hexlify(m.unique_id())
    TOPIC_LED=b'ap062/led'
    TOPIC_DISP=b'ap062/node_display'
    TOPIC_TEMP=b'ap062/temp'

    #print("Dispositivos: ",roms)
    mq = MQTTClient(CLIENT_ID,SERVER)
    mq.set_callback(sub_cb)
    mq.connect()
    mq.subscribe(TOPIC_LED)
    mq.subscribe(TOPIC_DISP)
    mq.subscribe(TOPIC_TEMP)
    print("Conectado ao %s, inscrito no topico %s" % (SERVER,TOPIC_LED))
    print("Conectado ao %s, inscrito no topico %s" % (SERVER, TOPIC_DISP))
    try:
        while 1:
            mq.wait_msg()

    finally:
        mq.disconnect()

#    blink_led()
    #i2c_test()
