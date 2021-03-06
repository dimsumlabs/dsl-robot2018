"""Load a list of possible wifi networks and connect to the first matching"""

# TODO
# - set DHCP client hostname properly:
#       xxx.config(dhcp_hostname=yyy) where yyy is based on macaddr
# - in access_point() if ssid is none, generate one the same as hostname above
# - If no wifi found to join, call access_point()
# - have a function to append new network to the wifi_cfg.py file


import network

# uses a wifi_cfg.py
# AP = list()
# AP = [b'apssid', b'appsk']
# WIFI = list()
# WIFI += [[b'ssid', b'psk']]

def access_point(ssid, psk):
    ap = network.WLAN(network.AP_IF) 
    ap.active(True)
    ap.config(essid=ssid)
    ap.config(authmode=3, password=psk)

def match_wifi(scan, wifi):
    for found in scan:
        for known in wifi:
            if found[0] == known[0]:
                return known
    return None, None

def connect():
    sta = network.WLAN(network.STA_IF)

    if sta.isconnected() == True:
        return True

    sta.active(True)
    scan = sta.scan()

    # try to load the wifi settings
    try:
        import wifi_cfg
        WIFI = wifi_cfg.WIFI
    except ImportError:
        WIFI = list()

    ssid, psk = match_wifi(scan, WIFI)
    if ssid:
        sta.connect(ssid, psk)
    else:
        print('No matching network found\n')
