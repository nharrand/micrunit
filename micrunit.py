#!/usr/bin/python2.7

# -*-coding:Utf-8 -*

import os
from os import listdir
from os.path import isfile, join
import serial
import time
from config import testDir, serialPort, serialBaudRate, timeout, initDelay
from testCase import runTestCase

print("--------------------------------")
print("|           micrunit           |")
print("--------------------------------")

# Open serial port
ser = serial.Serial(serialPort, serialBaudRate, timeout=timeout)
print("[INFO] Serial port:", ser.name)

# Verifications
assert ser.is_open, "[FAILURE] Failed to open serial port."
assert os.path.isdir(testDir), "[FAILURE] Test directory not found."
time.sleep(initDelay)

# Get all json files contained in testDir
testFiles = [f for f in listdir(testDir) if isfile(join(testDir, f)) and f.endswith('.json')]

print("tests:", ', '.join(testFiles))

# Run tests
for f in testFiles:
	print("--------------------------------")
	runTestCase(join(testDir, f), ser)

ser.close()
print("--------------------------------")
