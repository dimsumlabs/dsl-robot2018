# Functions relative to LED
# 	ledcount = number of time the LED will flash
# 	ledsleep = sleeping time in milliseconds
# 	ledpin# = pin number for the LED
# 	on the ESP8266 the led.on() switch off the LED

#TODO
#	Hamish to add his code for pulsing 1 LED via PWM

import machine
import time


# Allow to flash 1 LED
def lflash(ledcount, ledsleep, ledpin):
	led = machine.Pin(ledpin, machine.Pin.OUT)
	led.on()
	for i in range(ledcount):	
		led.off()
		time.sleep_ms(ledsleep)
		led.on()
		time.sleep_ms(ledsleep)
	led.on()


# Allow to flash in alternace 2 distinctive LED
def lflash2(ledcount, ledsleep, ledpin1, ledpin2):
	led1 = machine.Pin(ledpin1, machine.Pin.OUT)
	led2 = machine.Pin(ledpin2, machine.Pin.OUT)
	led1.on()
	led2.on()
	for i in range(ledcount):	
		led1.off()
		led2.on()
		time.sleep_ms(ledsleep)
		led1.on()
		led2.off()
		time.sleep_ms(ledsleep)
	led1.on()
	led2.on()


	

