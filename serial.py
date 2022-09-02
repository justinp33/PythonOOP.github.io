"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        "Get initial start number"
        self.counter = start

    def generate(self):
        "Generate number starting at start parameter and add one every time it is called"
        self.counter +=1
        return self.counter - 1

    def reset(self):
        self.counter = 0

