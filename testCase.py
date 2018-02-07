# -*-coding:Utf-8 -*

import os
import json

def runTestCase(file, serialport):
	print "[Info] Running ", file
	testcases = json.load(open(file))
	failures = 0
	for tc in testcases:
		print "[Info] Running ", tc['name']
		for seq in tc['sequence']:
			print "[Info] Input ", seq['input']
			print "[Info] Expecting ", seq['output']
			serialport.write(bytes(seq['input'] + "\n"))
			failed = False
			for expected in seq['output']:
				print "[Info] waiting for  ", expected
				expected += '\n'
				output = serialport.readline()
				if len(output) == 0:
					print "[FAILURE] timeout "
					failures += 1
					failed = True
					break
				elif output == expected:
					print "[INFO] OK"
				else:
					print "[FAILURE] got ", output
					failures += 1
					failed = True
					break
			if failed:
				break
	
	print "--------------------------------"
	print "[INFO] test: ", len(testcases), ", failures: ", failures
	print "--------------------------------"
	serialport.write(bytes('\n'))
