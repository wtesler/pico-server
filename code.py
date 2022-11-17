from network import WLAN, AP_IF
from access_point import start_access_point
from server import start_server

ssid = 'Pico Server'
password = '123456789'

    
wlan = WLAN(AP_IF)
wlan.config(ssid=ssid, password=password)

# wlanState = wlan.active();
# print(f'Starting WLAN state: {wlanState}')

wlan.active(False)

start_access_point(wlan)
start_server(wlan)

wlan.active(False)
print('Stopping wlan')
