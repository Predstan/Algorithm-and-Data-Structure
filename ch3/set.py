# Implementation of Set ADT using Python List

class Set:

    # Creates an Empty Set instance
    def __init__(self, *initialElements):

        self.elements = list(initialElements)


    # Returns the Length of elements in the set
    def __len__(self):
        return len(self.elements)

    # Returns True if element is contained in the set
    def __contains__(self, element):
        return element in self.elements

    # Adds Elements only when Element is not already in the set
    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)

    # Removes the element if already in the list
    def remove(self, element):
        assert element in self, "The element not in Set"
        self.elements.remove(element)

    # Determines if two sets are equal
    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            return self.isSubsetOf(setB)

    # Returns True if set A is a subset of Set B
    def isSubsetOf(self, setB):
        for element in self.elements:
            if element not in setB.elements:
                return False
        return True

    # Returns True if Set is a proper Set
    def properSet(self, setB):
        return self.isSubsetOf(setB) and self != setB

    # Returns the Items in the Set as String
    def __str__(self):
       return '{%s}' % str(self.elements).strip("[]")


    # Returns the Union of Set A and Set B as a new set
    def union(self, setB):
        newSet = Set()
        newSet.elements.extend(self)
        for element in setB:
            if element not in self:
                newSet.elements.append(element)
        return newSet

    # Returns the Intersect of Set A and Set B  as a new set
    def intersect(self, setB):
        newSet = Set()
        for element in self:
            if element in setB:
                newSet.add(element)
        return newSet

    # Returns the difference unique elements of Set A and Set B as a new set
    def difference(self, setB):
        newSet = Set()
        for element in self:
            if element not in setB:
                newSet.add(element)
        return newSet

    # Returns the Union of 2 Sets using python operator add
    def __add__(self, setB):
        newSet = Set()
        newSet.elements.extend(self)
        for element in setB:
            if element not in self:
                newSet.elements.append(element)
        return newSet

     # Returns the intersect of 2 Sets using python operator mul
    def __mul__(self, setB):
        newSet = Set()
        for element in self:
            if element in setB:
                newSet.add(element)
        return newSet

    # Returns the difference of 2 Sets using python operator sub
    def __sub__(self, setB):
        newSet = Set()
        for element in self:
            if element not in setB:
                newSet.add(element)
        return newSet

    # Determines if a Set is a Subset of another Set B
    def __lt__(self, setB):
        for element in self:
            if element not in setB:
                return False
        return True

    # Iterates over the set
    def __iter__(self):
        return SetIterator(self.elements)



class SetIterator(Set):

    # Creates an instance of the list
    def __init__(self, elements):
        self.elements = elements
        self.ndx = 0

    # Returns the Iteration
    def __iter__(self):
        return self.elements

    # Returns the Next Element
    def __next__(self):
        if self.ndx < len(self.elements):
            new = self.elements[self.ndx]
            self.ndx += 1
            return new

        raise StopIteration


setA = Set()
setA.add(0)
setA.add(2)
setA.add(3)
setA.add(1)
setA.add(1)
setA.add(6)

setB = Set()
setB.add(1)
setB.add(1)
setB.add(2)
setB.add(8)

print(setB)
print(setA)
print(setA * setB)
print(setA - setB)
print(setA + setB)
print(6 in setA)