# Implementation of Vector ADT using Linked List

class Vector:
    # Creates an empty Vector
    def __init__(self):
        self.Vectorhead = None
        self.tail = self.Vectorhead

    # Returns the length of the vector
    def __len__(self):
        number = 0
        curNode = self.Vectorhead
        while curNode is not None:
            number += 1
            curNode = curNode.next
        return number

    # Determines if an element is in the Vector
    def __contains__(self, item):
        curNode = self.Vectorhead

        while curNode is not None and curNode.data != item:
            curNode = curNode.next

        if curNode is not None and curNode.data == item:
            return True

        else:
            return False

    # Returns the item at an index
    def __getitem__(self, ndx):
        assert ndx >= 0 and ndx < len(self),\
             "index Out of Range"

        curNode = self.Vectorhead
        n = 0

        while curNode is not None and n < ndx:
            n += 1
            curNode = curNode.next
        
        if ndx == 0:
            return self.Vectorhead.data

        if curNode is not None and n == ndx:
            return curNode.data

    # Sets the value of an index
    def __setitem__(self, ndx, value):

        curNode = self.Vectorhead
        newNode = VectorNode(value)
        preNode = None
        n = 0

        # Contineus to  iterate the list until it reaches the index 
        while curNode is not None and n < ndx:
            n += 1
            preNode = curNode
            curNode = curNode.next
        
        if ndx == 0:
            if self.Vectorhead is None:
                self.Vectorhead = newNode
            else:
                newNode.next = curNode.next
                self.Vectorhead = newNode

        elif n == ndx:
            if curNode is not None:
                curNode.data = value
            else:
                preNode.next = newNode
                self.tail = newNode

    # Appends an element to the last of of the vector
    def append(self, value):
        newNode = VectorNode(value)
        if self.Vectorhead is None:
            self.Vectorhead = newNode
            self.tail =  newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    # Insert an element to an indext in the List
    def insert(self, ndx, value):
        curNode = self.Vectorhead
        preNode = None
        newNode = VectorNode(value)
        n = 0

        while curNode is not None and n < ndx:
            n += 1
            preNode = curNode
            curNode = curNode.next

        if ndx == 0:
            newNode.next = curNode
            self.Vectorhead = newNode

        else:
            if curNode is not None:
                newNode.next = curNode
                preNode.next = newNode               
            else:
                preNode.next = newNode
                self.tail = newNode

    # Remove an item from the vector
    def remove(self, item):
        assert item in self, " Item not in List"
        
        curNode = self.Vectorhead
        preNode = None

        while curNode is not None and curNode.data != item:
            preNode = curNode
            curNode = curNode.next

        if curNode is not None and curNode.data == item:
            if curNode == self.Vectorhead:
                self.Vectorhead = curNode.next
                return curNode.data
            elif curNode == self.tail:
                item = preNode.next.data
                preNode.next = None
                self.tail = preNode
                return item
            else:
                preNode.next = curNode.next
                return curNode.data
    # Returns the items in the vector as a string
    def __str__(self):
        result = ""
        curNode = self.Vectorhead
        while curNode is not None:
            if curNode.next is not None:
                result += str(curNode.data) + ", "

            else:
                result += str(curNode.data)
    
            curNode = curNode.next

        return '[%s]' % result

    # Removes an Index from the List and
    # Shift the List to cover the space
    def pop(self, ndx):
        assert ndx >= 0 and  ndx < len(self),\
             " Index out of Range"
        curNode = self.Vectorhead
        preNode = None
        n = 0

        while curNode is not None and n < ndx:
            n += 1
            preNode = curNode
            curNode = curNode.next

        if ndx == 0 and curNode is not None:
            self.Vectorhead = curNode.next

        elif n == ndx and curNode is not None:
            if curNode == self.tail:
                preNode.next = None
                self.tail = preNode 
            else:
                preNode.next = curNode.next

    # Returns the indext of an item
    def indexOf(self, item):
        assert item in self, " Item not in List"
        curNode = None
        n = 0

        while curNode is not None and curNode.data != item:
            n += 1
            curNode = curNode.next

        if curNode is not None and curNode.data == item:
            return n

    # Extends the List with another List
    def extend(self, VectorB):
        self.tail.next = VectorB.Vectorhead
        self.tail = VectorB.tail

    # Returns the Indices from and to
    def SubVector(self, From, to):
        curNode = self.Vectorhead
        n = 0
        newNode = None
        newVector = Vector()

        while curNode is not None and n < From:
            n += 1
            curNode = curNode.next

        newNode = VectorNode(curNode.data)
        newVector.Vectorhead = newNode
        newVector.tail = newVector.Vectorhead
        curNode = curNode.next
        n += 1

        while curNode is not None and n < to:
            n += 1
            newNode = VectorNode(curNode.data)
            newVector.tail.next = newNode
            newVector.tail = newNode

            curNode = curNode.next

        return newVector

    # Returns the Iterator of the Vector List
    def __iter__(self):
        return VectorIterator(self.Vectorhead)

# The LinkedList for Vector
class VectorNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# Class for Vector Iterator
class VectorIterator(object):
    def __init__(self, head):
        self.head = head


    def __iter__(self):
        return self.head

    def __next__(self):
        
        if self.head is not None:
            item = self.head.data
            self.head = self.head.next
            return item
        else:
            raise StopIteration


#TEST

A = Vector()
A.append(9)
A.append(4)
A.append(5)
A.insert(0, 3)
A.insert(1, 2)
A.insert(2, 7)
A.pop(2)
A.pop(3)
A.pop(0)
A.remove(9)
A.append(4)
A.remove(4)


B = Vector()
B.append(90)
B.append(90)
B.append(90)
B.append(90)
B.append(90)
B.append(90)
B.append(90)
B.append(90)
A.append(0)
A.append(0)
A.append(0)
A.append(0)
A.append(0)
A.append(0)
A.append(0)
A.extend(B)
print(35 in A)
B = A.SubVector(7, 10)
print(A)
print(B)