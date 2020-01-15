from gpiozero import LED, Buzzer

red_led = LED(18)
blue_led = LED (24)
buzzer = Buzzer(22)

def blue_on():
    blue_led.on()

def system_on():
    blue_led.off()
    red_led.on()
    buzzer.on()

def system_off():
    buzzer.off()
    red_led.off()
    blue_led.on()

def blue_off():
    blue_led.off()
