#!/usr/bin/python3

# -*-coding:Utf-8 -*

import os
from os import listdir
from os.path import isfile, join
import serial
from config import testDir, serialPort, serialBaudRate, timeout
import json

def simulateTestCase(file, serialport):
	print "[Info] Running ", file
	testcases = json.load(open(file))
	for tc in testcases:
		print "[Info] Running ", tc['name']
		for seq in tc['sequence']:
			incoming = serialport.readline()
			print "in: ", incoming
			expected = seq['input'] + '\n'
			if incoming == expected:
				for towrite in seq['output']:
					print "write: ", towrite
					serialport.write(bytes(towrite + "\n"))
			else:
				print "got <", incoming, ">, len: ", len(incoming) 
	print "--------------------------------"
	serialport.write(bytes('\n'))

print "--------------------------------"
print "|             test             |"
print "--------------------------------"

# Open serial port
ser = serial.Serial(serialPort, serialBaudRate, timeout=timeout)
print "[INFO] Serial port: ", ser.name

# Verifications
assert ser.is_open, "[FAILURE] Failed to open serial port."
assert os.path.isdir(testDir), "[FAILURE] Test directory not found."

# Get all json files contained in testDir
testFiles = [f for f in listdir(testDir) if isfile(join(testDir, f)) and f.endswith('.json')]

print "tests: ", testFiles

# Run tests
for f in testFiles:
	print "--------------------------------"
	simulateTestCase(join(testDir, f), ser)

ser.close()
print "--------------------------------"
