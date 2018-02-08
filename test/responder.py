#!/usr/bin/python3

# -*-coding:Utf-8 -*

import os
from os import listdir
from os.path import isfile, join
import serial
from config import testDir, serialPort, serialBaudRate, timeout
import json
import time
from config import endChar

#endChar = '.'


def readResp(serialport):
	buf = ""
	while True:
		while serialport.inWaiting() <= 0:
			time.sleep(.1)
		while serialport.inWaiting() > 0:
			inByte = serialport.read(1)
			#print("in",inByte)
			if inByte == bytes(endChar, "ascii"):
				#print("ok")
				return buf
			else:
				buf += inByte.decode("ascii")

def simulateTestCase(file, serialport):
	print("[Info] Running ", file)
	testcases = json.load(open(file))
	for tc in testcases:
		print("[Info] Running ", tc['name'])
		for seq in tc['sequence']:
			incoming = readResp(serialport)
			print("in: ", incoming)
			expected = seq['input']
			if incoming == expected:
				for towrite in seq['output']:
					print("write: ", towrite)
					serialport.write(bytes(towrite + endChar, "ascii"))
			else:
				print("got <", incoming, ">, len: ", len(incoming))
	print("--------------------------------")

print("--------------------------------")
print("|             test             |")
print("--------------------------------")

# Open serial port
ser = serial.Serial(serialPort, serialBaudRate, timeout=timeout)
print("[INFO] Serial port: ", ser.name)

# Verifications
assert ser.is_open, "[FAILURE] Failed to open serial port."
assert os.path.isdir(testDir), "[FAILURE] Test directory not found."

# Get all json files contained in testDir
testFiles = [f for f in listdir(testDir) if isfile(join(testDir, f)) and f.endswith('.json')]

print("tests: ", testFiles)

# Run tests
for f in testFiles:
	print("--------------------------------")
	simulateTestCase(join(testDir, f), ser)

ser.close()
print("--------------------------------")
