class IterableInteger(int):
    """ An Interable Integer """
    def __iter__(self):
        """ 
            Handles all iteration on the object
            Simply returns the object at the beginnging 
            of the loop
        """
        self.current = -1
        return self
    
    def __next__(self):
        """ Moves the iterator to the next value """
        if self.current == -1:  
            self.current = self.real
        if self.current == -2:
            self.current = self.real
            raise StopIteration 
        if 10 > self.current >= 1:
            digit = int(self.current)
            self.current = -2
            return digit
        digit = self.current % 10
        self.current = self.current / 10
        return int(digit)
