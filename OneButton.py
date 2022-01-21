
# How to Detect Short, Long, and Double Clicks with Arduino
# https://www.youtube.com/watch?v=TwM1sp2IXYI
# My Code: 
# https://pastebin.com/xEr5kV5j
# https://github.com/mathertel/OneButton

# 超圖解ESP32深度實作
# https://swf.com.tw/?p=1498
# 第3章 物件導向程式設計與自製Arduino程式庫
# 動手做3-1可分辨「按一下」和「長按」動作的開關

# https://www.flag.com.tw/DL.asp?F1794

# python function parameter another function
# 傳入函式，作為參數
# https://www.geeksforgeeks.org/passing-function-as-an-argument-in-python/

from machine import Pin
import time

class OneButton:
	def __init__(self, pin, ONState, pullup):

		self._ONState = ONState
		self._pullup = pullup
		self._pinVar = pin
		
		self._pressTime = 0
		self._debounceTime = 30
		self._longPressTime = 500
		self._lastHoldTime = 0
		self._holdTime = 200
		self._isPressed = False
		self._isLongPressed = False
		self._status = None
		self._clickFunc = None
		self._longPressStopFunc = None
		
		if pullup == True:
			self._pin = Pin(pin, Pin.IN, Pin.PULL_UP)
		else:
			self._pin = Pin(pin, Pin.IN)
			
	def config(self, debounceTime = 30, longPressTime = 500):
		self._debounceTime = debounceTime
		self._longPressTime = longPressTime
			
	def attachClick(self, Func):
		self._clickFunc = Func
	
	def attachLongPressStop(self, Func):
		self._longPressStopFunc = Func
		
	def ticks(self):
		self._status = None
		# print("ticks")
	
		if self._pin.value() == self._ONState:
			
			# 按下
			if self._isPressed == False:
				self._isPressed = True
				self._pressTime = time.ticks_ms()
			
			if self._isPressed == True:
				PressTime = time.ticks_ms() - self._pressTime
				# print(PressTime)
				
				# 持續按下
				if self._isLongPressed == True and PressTime > self._holdTime:
					self._lastHoldTime = time.ticks_ms()
				
				# 長按
				if self._isLongPressed == False and PressTime > self._longPressTime:
					self._isLongPressed = True
		# 放開按鍵
		else:
		
			if self._isPressed == True:
				PressTime = time.ticks_ms() - self._pressTime
			
				if self._isLongPressed == True :
					self._isPressed = False
					self._pressTime = 0
					
					# and self._longPressStopFunc != None:
					self._isLongPressed = False
					self._lastHoldTime = 0
					# self._status = self._longPressStopFunc
					
					# print("longPressStopFuncParam")
					print(PressTime)
					self._longPressStopFunc(self._pinVar, PressTime)
					return
					
				
				if self._isLongPressed == False and PressTime > self._debounceTime:
					self._isPressed = False
					self._pressTime = 0

					#print("clickFuncParam")
					print(PressTime)
					self._clickFunc(self._pinVar, PressTime)
					return
					
					
			
			self._pressTime = 0
			self._isPressed = False





