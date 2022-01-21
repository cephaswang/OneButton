from OneButton import OneButton
from machine import Timer

# Python 中的回撥函式
# https://www.delftstack.com/zh-tw/howto/python/python-callback-function/

# https://www.youtube.com/watch?v=iUrUf5ijiWs

def singleclick():
	print("singleclick")
	
def longclick():
	print("longclick")
	
TE1 = OneButton(23, 0 ,True)
TE1.attachClick(singleclick)
TE1.attachLongPressStop(longclick)
# TE1.config(50,2000)


def CheckPins(pin):
	TE1.ticks()


#global timer
#timer = Timer(-1)
#timer.init(period=10, mode=Timer.PERIODIC, callback=CheckPins)


while True:
	CheckPins(0)
