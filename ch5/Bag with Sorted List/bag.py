# Implementation of Bag ADT using Sorted list and best Time Complexity
class bag:
    # Creates and empty bag
    def __init__(self):

        self.elements = list()

    # Returns the length of a bag
    def __len__(self):
        return len(self.elements)

    # Determines if item is contained in the Bag
    def __contains__(self, element):
        first = self.findFirstposition(element)
        return first < len(self) and element == self.elements[first]

    # Adds item to the bag
    def add(self, element):
        first = self.findFirstposition(element)
        self.elements.insert(first, element)

    # Returns the number of an item in the Bag
    def numOf(self, item):
        assert item in self.elements, " Item not in Bag"
        first, last = self.findPosition(item)
        return last - first + 1
    
    # Removes all entry of an item in the bag
    def remove(self, item):
        assert item in self.elements, " Item not in Bag"
        first, last = self.findPosition(item)
        for i in range(first, last+1):
            self.elements.pop(first)
        
    # Finds the first position of an item
    def findFirstposition(self, element):
        low = 0
        high = len(self.elements) - 1

        # Continues to divide elements in the bag until it sees the fist entry of item
        while low <= high:
            mid = (high + low) // 2

            # Determines if the taget is met and target is larger than preceding value
            if (self.elements[mid] == element\
                and (self.elements[mid-1] < element or mid == 0)):
                return mid

            # Determines if item found is smaller than the item
            elif self.elements[mid] < element:
                low = mid + 1

            # Determines if item found is larger than the item
            else:
                high = mid - 1

        return low # Return the value an item is suppose to be if not found

    # Returns the last position of an item
    def findLastPosition(self, element):
        low = 0
        high = len(self.elements) - 1

        # Continues to divide elements in the bag until it sees the last entry of item
        while low <= high:

            mid = (high + low) // 2

            # Determines if the taget is met and target is smaller than value after
            if ((self.elements[mid] == element) and \
                (high == low or self.elements[mid+1] > element)):
                return mid

            # Determines if item found is larger than the item
            elif self.elements[mid] > element:
                high = mid - 1

            # Determines if item found is larger than the item 
            else:
                low = mid + 1

        return low

    # Returns the first and last postion of the item
    def findPosition (self, element):
        first = self.findFirstposition(element)
        last = self.findLastPosition(element)
        return first, last

    # Iterator for the bag elements
    def __iter__(self):
        return BagIterator(self.elements)

# Iterator for Bag ADT
class BagIterator:
    
    def __init__(self, theElements):
        self.theElements = theElements
        self.ndx = 0

    def __iter__(self):
        return self.theElements

    def __next__(self):
        if self.ndx < len(self.theElements):
            value = self.theElements[self.ndx]
            self.ndx += 1
            return value

        raise StopIteration


# TEST   
hi = bag()
hi.add(1)
hi.add(1)
hi.add(1)
hi.add(1)
hi.add(1)
hi.add(2)
hi.add(3)
hi.add(90)
hi.add(140)

hi.remove(140)


print(hi.numOf(1))

print(90 in hi)