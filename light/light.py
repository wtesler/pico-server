def blink_light():
    from machine import Pin, Timer

    led = Pin("LED", Pin.OUT)
    timer = Timer()

    def tick(timer):
        led.toggle()
        
    timer.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)


def toggle_light():
    from machine import Pin

    led = Pin("LED", Pin.OUT)
    led.toggle()


def switch_light(isOn):
    from machine import Pin

    led = Pin("LED", Pin.OUT)
    led.value(1 if isOn else 0)