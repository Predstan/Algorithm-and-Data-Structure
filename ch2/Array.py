# Implements a 1-D Array Using the ctypes Module
import ctypes

class Array:
    # Creates the Array with the givem size of the Array
    def __init__(self, size):
        assert size > 0, 'Array Must be greater than 0'
        self.size = size

        ArrayTypes = ctypes.py_object * size
        self.slots = ArrayTypes()

        self.clear(0)

    # Returns the size of the Array
    def __len__(self):
        return self.size

    # Returns the item in the given index
    def __getitem__(self, index):
        assert index >= 0 and index < len(self.slots), "Index out of range"
        return self.slots[index]

    # Sets a value to the index
    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self.slots), "Index out of range"
        self.slots[index] = value

    # Sets the Value to the Array
    def clear(self, value):
        for i in range(self.size):
            self.slots[i] = value
    # Iterating over the array
    def __iter__(self):
        return Arrayiterator(self.slots)



class Arrayiterator:
    # Creates 
    def __init__(self, thelist):
        self.list = thelist
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx <len(self.list):
            ent = self.list[self.idx]
            self.idx+=1
            return ent
        else:
            raise StopIteration
