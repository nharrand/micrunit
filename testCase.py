# -*-coding:Utf-8 -*

import os
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
def flush(serialport):
	while serialport.inWaiting() > 0:
		inByte = serialport.read(1)

def runTestCase(file, serialport):
	print("[INFO] Running", file)
	#time.sleep(2)
	flush(serialport)
	testcases = json.load(open(file))
	failures = 0
	for tc in testcases:
		print("[INFO] Running", tc['name'])
		for seq in tc['sequence']:
			flush(serialport)
			print("[INFO] -- Input", seq['input'])
			print("[INFO] -- Expecting", ', '.join(seq['output']))
			wl = serialport.write(bytes(seq['input'] + endChar, "ascii"))
			#print("wrote ", wl, " bytes", bytes(seq['input'] + endChar))
			#serialport.flushOutput();
			time.sleep(1)
			failed = False
			for expected in seq['output']:
				print("[Info] -- waiting for", expected)
				#output = serialport.readline()
				output = readResp(serialport)
				if len(output) == 0:
					print("[FAILURE] timeout ")
					failures += 1
					failed = True
					break
				elif output == expected:
					print("[INFO] -- -- OK")
				else:
					print("[FAILURE] got", output)
					failures += 1
					failed = True
					break
			if not failed and serialport.inWaiting() > 0:
				print("[FAILURE] extra", serialport.read(serialport.inWaiting()))
				failures += 1
				failed = True
			if failed:
				break
	
	print("--------------------------------")
	print("[INFO] test:", len(testcases), ", failures:", failures)
	print("--------------------------------")
	serialport.write(bytes(endChar, "ascii"))
