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
        "Creates the serial object"
        self.counter =start
        self.start = start

    def generate (self):
        "It should return the next sequential number"
        actual_value =  self.counter
        self.counter = self.counter + 1
        return actual_value  
      
    def reset(self):
        "Resets the number back to the original start number"
        self.counter =  self.start
       
