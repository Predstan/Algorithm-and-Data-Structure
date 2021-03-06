# Implementation of SET ADT using Sorted List

class Set:
    # Creates an empty set instance.
    def __init__(self, *initialElement):
        self.elements = list()

        for i in range(len(initialElement)):
            self.add(initialElement[i])


    # Returns the number of items in the set
    def __len__(self):
        return len(self.elements)

    # Determines if an element is in the set.
    def __contains__(self, element):
        ndx = self.findPosition(element)
        return ndx < len(self) and self.elements[ndx] == element

    # Adds a new unique element to the set.
    def add(self, element):
        if element not in self.elements:
            ndx = self.findPosition(element)
            self.elements.insert(ndx, element)

    # Removes an element from the set.
    def remove(self, element):
        assert element in self.elements, "Element not in Set"
        ndx = self.findPosition(element)
        self.elements.pop(ndx)

    # Determines if this set is a subset of setB.
    def isSubsetOf(self, setB):
        for element in self.elements:
            if element not in setB.elements:
                return False
        return True
    
    # Determines if Set is a proper Set
    def properSet(self, setB):
        return self.isSubsetOf(setB) and self != setB

    # Returns the Items in the Set as String
    def __str__(self):
        return '{%s}' % str(self.elements).strip("[]")

    # Returns the Union of Set A and Set B as a new set
    def union(self, setB):
        newSet = Set()
        a = 0
        b = 0
        # Merge the two lists together until one is empty.
        while a < len(self) and b < len(setB):
            valueA = self.elements[a]
            valueB = setB.elements[b]
            if valueA < valueB:
                newSet.elements.append(valueA)
                a += 1
            elif valueA > valueB:
                newSet.elements.append(valueB)
                b += 1
                
            # Only one of the two duplicates are appended.
            else:
                newSet.elements.append(valueA)
                a += 1
                b += 1

        # If listA contains more items, append them to newList.        
        while a < len(self):
            newSet.elements.append(self.elements[a])
            a += 1
        
        # Or if listB contains more, append them to newList.
        while b < len(setB):
            newSet.elements.append(setB.elements[b])
            b +=  1

        return newSet

    # Returns the Intersect of Set A and Set B as a new set
    def intersect(self, setB):
        newSet = Set()
        for element in self.elements:
            if element in setB.elements:
                ndx = newSet.findPosition(element)
                newSet.elements.insert(ndx, element)
        return newSet
    
    # Returns the difference unique elements of Set A and Set B as a new set
    def difference(self, setB):
        newSet = Set()
        for element in self.elements:
            if element not in setB.elements:
                ndx = newSet.findPosition(element)
                newSet.elements.insert(ndx, element)
        return newSet

    # Determines if 2 Sets are equal
    def __eq__(self, setB):

        if len(self) != len(setB):
            return False
        else: 
            for i in range(len(self)):
                if self.elements[i] != setB.elements[i]:
                    return False
            return True

    # Returns the union of unique elements of Set A and Set B as a new set
    def __add__(self, setB):
        return self.union(setB)

    # Returns the difference unique elements of Set A and Set B as a new set
    def __sub__(self, setB):
        return self.difference(setB)

    # Returns the intersect of Set A and Set B as a new set
    def __mul__(self, setB):
        return self.intersect(setB)

    # Determines if Set A is a subset of Set B 
    def __lt__(self, setB):
        return self.isSubsetOf(setB)

    # Iterates over the Set Elements
    def __iter__(self):
        return SetIterator(self.elements)

    # Finds the position of the element within the ordered list.
    def findPosition(self, element):
        
        low = 0
        high = len(self) - 1
        # Repeatedly subdivide the sequence in half until the target is found.
        while low <= high:
            # Find the midpoint of the sequence.
            mid = (high + low) // 2
            
            # Does the midpoint contain the target?
            if self.elements[mid] == element:
                return mid
        
            # Or does the target precede the midpoint?
            elif self.elements[mid] > element:
                high = mid - 1

            # Or does it follow the midpoint?
            else:
                low = mid + 1

        return low


class SetIterator:

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


# TEST
setA = Set(5, 6, 9)
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

setB.remove(8)
print(setA + setB)
print(setB)
print(setA)
print(setA * setB)
print(setA - setB)
print(6 in setA)

print(setA == setB)

