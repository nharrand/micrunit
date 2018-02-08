# -*-coding:Utf-8 -*

# Path to test directory. It should contains json describing test cases.
testDir = "test/testcases"

# Path to serial
#serialPort = '/dev/pts/28'
serialPort = '/dev/pts/20'
# Baudrate
serialBaudRate = '9600'
# Time to wait before declaring a test as failed
timeout = 5 # not used

#Separation character ending an input
endChar = '\n'

#Time to wait between serial opening and the first input
initDelay = 3
