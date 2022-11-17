def start_access_point(wlan): 
    wlan.active(True)
    
    print("Attempting to start access point...")

    while wlan.active == False:
      pass

    print("Access point active.")
    
    print(wlan.ifconfig())
