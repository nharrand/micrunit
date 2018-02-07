# -*-coding:Utf-8 -*

import os
import json

def runTestCase(file, serialport):
	print "[Info] Running ", file
	testcases = json.load(open(file))
	for tc in testcases:
		print "[Info] Running ", tc['name']
		for seq in tc['sequence']:
			print "[Info] Input ", seq['input']
			print "[Info] Expecting ", seq['output']
			serialport.write(bytes(seq['input'] + "\n"))
			for expected in seq['output']:
				print "[Info] waiting for  ", expected
				output = serialport.readline()
				if len(output) == 0:
					print "[FAILURE] timeout "
				elif output is expected:
					print "[INFO] OK"
				else:
					print "[FAILURE] got ", output
	serialport.write(bytes('\n'))
