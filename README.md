# micrunit

Simple serial port unit testing harness

## Configuration

Modify the file `config.py` to change the serial port and the test directory (which contains json description of the tests).

## Run

Simply run `micrunit.py`

## Installation
micrunit requires the pyserial package. You can install it with pip
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
