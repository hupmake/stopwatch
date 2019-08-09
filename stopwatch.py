#!/usr/bin/python
# Python program that runs a stopwatch. Start, stop, reset, etc.
# So far, it will count seconds, minutes, and hours. It just goes. Stops on CTRL+C.

# version 0.2.0

# Imports!
# This is running on Linux, so we'll just do linuxy imports.
import time
import sys

# Building blocks!

hour_0 = 0
hour_1 = 0
mins_0 = 0
mins_1 = 0
secs_0 = 0
secs_1 = 0
key_press = input('Press s to start timer...')

def run_time():
	global hour_0
	global hour_1
	global mins_0
	global mins_1
	global secs_0
	global secs_1
	time_string = str(hour_0) + str(hour_1) + str(":") + str(mins_0) + str(mins_1) + str(":") + str(secs_0) + str(secs_1)

	print(time_string, end = '')
	print('\r', end = '', flush = 'True')

	if hour_1 == 9 and mins_0 == 5 and mins_1 == 9 and secs_0 == 5 and secs_1 == 9:
		secs_0 = 0
		secs_1 = 0
		mins_0 = 0
		mins_1 = 0
		hour_0 +=1
		hour_1 = 0
		time.sleep(1)

	elif mins_0 == 5 and mins_1 == 9 and secs_0 == 5 and secs_1 == 9:
		secs_0 = 0
		secs_1 = 0
		mins_0 = 0
		mins_1 = 0
		hour_1 +=1
		time.sleep(1)

	elif mins_1 == 9 and secs_0 == 5 and secs_1 == 9:
		secs_0 = 0
		secs_1 = 0
		mins_0 += 1
		mins_1 = 0
		time.sleep(1)

	elif secs_0 == 5 and secs_1 == 9:
		secs_0 = 0
		secs_1 = 0
		mins_1 += 1
		time.sleep(1)

	elif secs_1 < 9:
		secs_1 += 1
		time.sleep(1)

	elif secs_1 == 9:
		secs_1 = 0
		secs_0 += 1
		time.sleep(1)

while key_press == "s":
	run_time()
