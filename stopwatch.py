#!/usr/bin/python
# Python program that runs a stopwatch. Start and stop. No pause.
# So far, it will count seconds, minutes, and hours. It just goes.
# Stops on Ctrl-C and outputs the recorded time.

# version 1.0.0

# Imports!
import time

# Building blocks!
hour = 0
mins = 0
secs = 0

# The main (only?) function.
def run_time():
	global hour
	global mins
	global secs
# Set the time counter string an make it accessible outside of the func.
	run_time.time_string = str("{0:0=2d}".format(hour)) + str("h ") + str("{0:0=2d}".format(mins)) + str("m ") + str("{0:0=2d}".format(secs)) + str("s")
# Overwrite the used line when the script is running in real time.
	print(run_time.time_string, end = '')
	print('\r', end = '', flush = 'True')

	if hour == 23 and mins == 59 and secs == 59:
		hour = 0
		mins = 0
		secs = 0
		print("1 day reached. Timer ended.")
		raise KeyboardInterrupt
		time.sleep(1)

	elif mins == 59 and secs == 59:
		secs = 0
		mins = 0
		hour +=1
		time.sleep(1)

	elif secs == 59:
		secs = 0
		mins += 1
		time.sleep(1)

	elif secs < 59:
		secs += 1
		time.sleep(1)

while True:
	try:
		run_time()
		pass
# This catches the Ctrl-C
	except KeyboardInterrupt as e:
		print('\n Clocked',run_time.time_string)
		break
