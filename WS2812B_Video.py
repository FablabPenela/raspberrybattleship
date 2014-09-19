#!/usr/bin/python

import sys
import smbus
import cv2
import time

bus = smbus.SMBus(1)
address = 0x03

cap = cv2.VideoCapture(0)
cap.set(cv2.cv.CV_CAP_PROP_CONTRAST, 255)

outputWidth = 1
outputHeight = 1
outputSize = (outputWidth, outputHeight)

for x in range(1000):
	success, frame = cap.read()
	if success == True:
		print x
		frame = cv2.resize(frame, outputSize, interpolation = cv2.INTER_AREA)
		frame = cv2.cvtColor(frame, cv2.cv.CV_BGR2RGB)
		for i in range(outputHeight):
			for j in range(outputWidth):
				led = i * outputWidth + j
				rgb = frame[i, j].tolist()
				try:
					bus.write_block_data(address, led, rgb)
				except:
					cap.release()
		time.sleep(0.01)
cap.release()
