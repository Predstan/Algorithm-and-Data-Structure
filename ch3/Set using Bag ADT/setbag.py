# Implementation of the SET ADT using the Bag class

from bag import bag

class Set:
    # Creating an instance of the Set class with initial list
    def __init__(self, *thelist):

        # Creating the Bag from the Bag class
        self.elements = bag()

        # Adding all values in the list to the Bag  
        for value in thelist:
            self.elements.add(value)

    # Returns the number of element in the Set
    def __len__(self):
        return self.elements.length()

    # Adds an Element to the Set
    def add(self, element):
        if self.elements.contains(element) is False:
            self.elements.add(element)
    
    # Removes an Element from the Set 
    def remove(self, element):
        if self.elements.contains(element):
            self.elements.remove(element)

    # Determines if a set is equal to another
    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        return self.__lt__(setB)

    # Determines if set A is a Subset of Set B
    def isSubsetOf(self, setB):
        for element in iter(self.elements):
            if element not in iter(setB.elements):
                return False
        return True

    # Returns True if Set is a proper Set
    def properSet(self, setB):
        return self.isSubsetOf(setB) and self != setB

    # Returns the element in the Set as a string
    def __str__(self):
        return '{%s}' % str(iter(self.elements)).strip("[]")

    # Returns the Union of two Sets
    def union(self, setB):
        newSet = Set()
        newSet.elements.extend(self.elements)
        for element in setB.elements:
            if element not in self.elements:
                newSet.add(element)
        return newSet

    # Returns the intersect of two sets
    def intersect(self, setB):
        newSet = Set()
        for element in self.elements:
            if element in setB.elements:
                newSet.add(element)
        return newSet

    # Returns the difference of 2 sets
    def difference(self, setB):
        newSet = Set()
        for element in self.elements:
            if element not in setB.elements:
                newSet.add(element)
        return newSet

    # Iterates over the set
    def __iter__(self):
        return iter(self.elements)

    # Returns the Union of two Sets
    def __add__(self, setB):
        return self.union(setB)

    # Returns the difference of 2 sets
    def __sub__(self, setB):
        return self.difference(setB)

    # Returns the intersect of two sets
    def __mul__(self, setB):
        return self.intersect(setB)

    # Determines if set A is a Subset of Set B
    def __lt__(self, setB):
        return self.isSubsetOf(setB)




new = Set(8, 9, 0, 6, 5, 7)
old = Set(0, 8, 9, 1, 2, 3)
print(len(old))

diff = new.difference(old)

for value in old:
    print (value)




            

