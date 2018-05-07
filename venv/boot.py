'''
Script de configuração inicial

'''

import network
essid = 'Ap062'
password = 'ap_sp_!062mp'

sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    sta_if.active(True)
    sta_if.connect(essid, password)
    while not sta_if.isconnected():
        pass
print('network config:', sta_if.ifconfig())