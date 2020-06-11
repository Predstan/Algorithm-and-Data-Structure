# Implementation of Set ADT Using Sorted LinkedList

class Set:
    # Create a Set Instance with and optional elements
    def __init__(self, *InitialElements):

        self.Sethead = None
        self.tail = self.Sethead

        if len(InitialElements) != 0:
            for data in InitialElements:
                self.add(data)

    # Returns the length of the Set
    def __len__(self):
        curNode = self.Sethead
        number = 0
        while curNode is not None:
            curNode = curNode.next
            number +=1
        return number

    # Determines if an item is in the Set
    def __contains__(self, item):
        curNode = self.Sethead

        while curNode is not None and curNode.data < item:
            curNode = curNode.next

        if curNode is not None and curNode.data == item:
            return True

        return False

    # Adds an Item to the Set
    def add(self, item):
        curNode = self.Sethead
        preNode = None

        while curNode is not None and curNode.data < item:
            preNode = curNode
            curNode = curNode.next

        newNode = SetNode( item )
        newNode.next = curNode

        if curNode is not None and curNode.data > item:
            if curNode == self.Sethead:
                self.Sethead = newNode
            else:
                preNode.next = newNode


        elif curNode is None:
            if self.Sethead is None:
                self.Sethead = newNode
                self.tail = self.Sethead
            else:
                preNode.next = newNode
                self.tail = newNode


    # Remove an Item from the Set
    def remove(self, item):
        curNode = self.Sethead
        preNode = None

        while curNode is not None and curNode.data < item:
            preNode = curNode
            curNode = curNode.next

        if curNode is not None and curNode.data == item:
            if curNode == self.Sethead:
                self.Sethead = curNode.next
            else:
                preNode.next = curNode.next

        else:
            return "Item not in Set"

    # Determins if Set A is equal to Set B
    def __eq__(self, SetB):
        curNodeA = self.Sethead
        curNodeB = SetB.Sethead

        while curNodeA is not None and curNodeB is not None:
            if curNodeA.data == curNodeB.data:
                curNodeA = curNodeA.next
                curNodeB = curNodeB.next

            else:
                return False

        if curNodeA is None and curNodeB is None:
            return True

        else:
            return False

    # Determines if Set A s a subset of Set B
    def isSubsetOf(self, SetB):

        curNodeA = self.Sethead
        curNodeB = SetB.Sethead

        while curNodeA is not None and curNodeB is not None:
            if curNodeA.data == curNodeB.data:
                curNodeA = curNodeA.next
                curNodeB = curNodeB.next

            elif curNodeB.data > curNodeA.data:
                return False

            else:
                curNodeB = curNodeB.next

        if curNodeA is None:
            return True

        else:
            return False

    # Determines if Set A is  a proper Set of Set B
    def isProperSubset(self, SetB):
        return self.isSubsetOf(SetB) and self != SetB

    # Returns the  the Elements in the Set as str
    def __str__(self):

        curNode = self.Sethead
        data = list()
        while curNode is not None:
            data.append(curNode.data)
            curNode = curNode.next

        return '{%s}' % str(data).strip("[]")

    # Returns the Difference Between TWO SET
    def difference(self, SetB):
        newSet = Set()
        curNodeA = self.Sethead
        curNodeB = SetB.Sethead


        while curNodeA is not None and curNodeB is not None:
            if curNodeA.data == curNodeB.data:
                curNodeA = curNodeA.next
                curNodeB = curNodeB.next

            elif curNodeB.data > curNodeA.data:
                newSet.add(curNodeA.data)
                curNodeA = curNodeA.next

            else:
                newSet.add(curNodeB.data)
                curNodeB = curNodeB.next

        while curNodeA is not None:
            newSet.add(curNodeA.data)
            curNodeA = curNodeA.next

        while curNodeB is not None:
            newSet.add(curNodeB.data)
            curNodeB = curNodeB.next

        return newSet

    # Returns the Intersects of TWO SETS
    def intersect(self, SetB):
        newSet = Set()
        curNodeA = self.Sethead
        curNodeB = SetB.Sethead


        while curNodeA is not None and curNodeB is not None:
            if curNodeA.data == curNodeB.data:
                newSet.add(curNodeA.data)
                curNodeA = curNodeA.next
                curNodeB = curNodeB.next

            elif curNodeB.data > curNodeA.data:
                curNodeA = curNodeA.next

            else:
                curNodeB = curNodeB.next

        return newSet

    # Returns the Union of 2 Sets
    def union(self, SetB):
        newSet = Set()
        curNodeA = self.Sethead
        curNodeB = SetB.Sethead


        while curNodeA is not None and curNodeB is not None:
            if curNodeA.data == curNodeB.data:
                newSet.add(curNodeA.data)
                curNodeB = curNodeB.next
                curNodeA = curNodeA.next

            elif curNodeA.data > curNodeB.data:
                newSet.add(curNodeB.data)
                curNodeB = curNodeB.next

            else:
                newSet.add(curNodeA.data)
                curNodeA = curNodeA.next

        while curNodeA is not None:
            newSet.add(curNodeA.data)
            curNodeA = curNodeA.next

        return newSet


    def __add__(self, SetB):
        return self.union(SetB)

    def __sub__(self, SetB):
        return self.difference(SetB)

    def __mul__(self, SetB):
        return self.intersect(SetB)

    def __lt__(self, SetB):
        return self.isSubsetOf(SetB)

    def __iter__(self):
        return SetIterator(self.Sethead)

class SetNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class SetIterator:
    def __init__(self, head):
        self.head = head

    def __iter__(self):
        return self.head

    def __next__(self):

        if self.head is not None:
            item = self.head.data
            self.head = self.head.next
            return item

        raise StopIteration
setA = Set(5, 7, 9)
setA.add(0)
setA.add(2)
setA.add(0)
setA.add(3)
setA.add(1)
setA.add(1)
setA.add(6)
setA.add(-1)

setB = Set(5, 7, 9, 11)
setB.add(7)
setB.add(7)
setB.add(9)
setB.add(8)

setB.remove(8)
setC = Set(9, 5, 7, 11)


setD = Set(5, 7, 9, 11)
print(setA * setB)
print(setA - setB)
print(6 in setA)
print("\n")
print(setC == setD)
print(setC.isProperSubset(setD))

print(setD)
print(setC)
print(setB == setC)
print(setC == setD)

print(len(setD))
