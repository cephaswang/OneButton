from OneButton import OneButton
from machine import Timer
import time

# https://github.com/cephaswang/OneButton
# Python 中的回撥函式
# https://www.delftstack.com/zh-tw/howto/python/python-callback-function/

# https://www.youtube.com/watch?v=iUrUf5ijiWs

def singleclick(pinVar, PressTime):
	print("%d singleclick %d PressTime" % (pinVar, PressTime) )
	
def longclick(pinVar, PressTime):
	print("%d longclick %d PressTime" % (pinVar, PressTime) )
	
Coin_1 = OneButton(17, 0 ,True)
Coin_1.attachClick(singleclick)
Coin_1.attachLongPressStop(longclick)
# Coin_1.config(50,2000)

Coin_2 = OneButton(16, 0 ,True)
Coin_2.attachClick(singleclick)
Coin_2.attachLongPressStop(longclick)

def CheckPins(pin):
	A = Coin_1.ticks()
	B = Coin_2.ticks()


#global timer
#timer = Timer(-1)
#timer.init(period=10, mode=Timer.PERIODIC, callback=CheckPins)

time.sleep(1.5)

while True:
	CheckPins(0)
