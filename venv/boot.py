'''
Script de configuração inicial

'''

import network
import machine as m
import ssd1306
import time as t
i2c = m.I2C(scl=m.Pin(14),sda=m.Pin(12))
oled = ssd1306.SSD1306_I2C(128,32,i2c,0x3c)

essid = 'Ap062'
password = 'ap_sp_!062mp'

sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    sta_if.active(True)
    sta_if.connect(essid, password)
    while not sta_if.isconnected():
        pass



print('network config:', sta_if.ifconfig())
ip = str(sta_if.ifconfig())
t.sleep_ms(500)
oled.text("IP:",0,0)
oled.show()
oled.text(ip[2:15],5,16)
oled.show()