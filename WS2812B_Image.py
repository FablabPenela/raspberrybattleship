#!/usr/bin/python

import sys
import smbus
import time
import cv2
import cv

start = time.time()

bus = smbus.SMBus(1)
address = 0x03

frame = cv2.imread('Lenna.png')
outputWidth = 10
outputHeight = 6
outputSize = (outputWidth, outputHeight)
outputFrame = cv2.resize(frame, outputSize, interpolation = cv2.INTER_AREA)
outputFrame = cv2.cvtColor(outputFrame, cv.CV_BGR2RGB)
print outputFrame.shape

led = 0
i = 0
for i in range(outputHeight):
	for j in range(outputWidth):
		led = i * outputWidth + j
		rgb = outputFrame[i, j].tolist()
		#rgb = [0, 0, 0]
		bus.write_block_data(address, led, rgb)
		time.sleep(0.001)

end = time.time()
elapsed = end - start
print 'time taken: ', elapsed, 'seconds'
#print 'led: ', led, 'rgb: ', rgb
