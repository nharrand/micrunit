# micrunit
micrunit is a python3 serial port unit testing harness. 
It takes json test cases (describing inputs and expected outputs) and run them. Running a test case consist simply into feeding the inputs one by one to an USART while checking that the actual output correspond to the expected one.

## Configuration

Modify the file `config.py` to change the serial port and the test directory (which contains json description of the tests).

## Run

Simply run `python micrunit.py`

## Installation

micrunit requires:
 * python 3
 * the pyserial package. 

You can install pyserial with pip
```
pip install pyserial
```
or download it [here](https://pypi.python.org/pypi/pyserial).

## Test syntax

```json

[
	{
		"name": "Name of the test",
		"sequence": [
			{
				"input": "Char to feed to the serial port",
				"output": ["expected output 1", "expected output 2"]
			}
		]
	}
]

```

Note that a file can contain sveral test cases, a sequence can contain several pair (input, list of expected outputs).

See `test/testcases/test1.json` for more examples.

## Test the micrunit script

Open two connected virtual serial ports

```
socat -d -d pty,raw,echo=0 pty,raw,echo=0
```

Configure `test/config.py` and run `test/responder.py`
