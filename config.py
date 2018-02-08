# -*-coding:Utf-8 -*

# Path to test directory. It should contains json describing test cases.
testDir = "test/testcases"

# Path to serial
#serialPort = '/dev/pts/28'
serialPort = '/dev/ttyACM0'
# Baudrate
serialBaudRate = '9600'
# Time to wait before declaring a test as failed
timeout = 5

#Separation character ending an input
endChar = '\n'

#Time to wait between serial opening and the first input
initDelay = 3
