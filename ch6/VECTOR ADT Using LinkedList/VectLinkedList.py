class Vector:
    def __init__(self):
        self.Vectorhead = None
        self.tail = self.Vectorhead

    def __len__(self):
        number = 0
        curNode = self.Vectorhead
        while curNode is not None:
            number += 1
            curNode = curNode.next
        return number

    def __contains__(self, item):
        curNode = self.Vectorhead

        while curNode is not None and curNode.data != item:
            curNode = curNode.next

        if curNode is not None and curNode.data == item:
            return True

        else:
            return False

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

    def __setitem__(self, ndx, value):

        curNode = self.Vectorhead
        newNode = VectorNode(value)
        preNode = None
        n = 0

            
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

    def append(self, value):
        newNode = VectorNode(value)
        if self.Vectorhead is None:
            self.Vectorhead = newNode
            self.tail =  newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

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

    def __str__(self):
        result = list()
        curNode = self.Vectorhead
        while curNode is not None:
            result.append(curNode.data)
            curNode = curNode.next

        return str(result)

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

    def indexOf(self, item):
        assert item in self, " Item not in List"
        curNode = None
        n = 0

        while curNode is not None and curNode.data != item:
            n += 1
            curNode = curNode.next

        if curNode is not None and curNode.data == item:
            return n


    def extend(self, VectorB):
        self.tail.next = VectorB.Vectorhead
        self.tail = VectorB.tail

    def SubVector(self, From, to):
        curNode = self.Vectorhead
        n = 0
        m = 0
        newVector = Vector()

        while curNode is not None and n < From:
            n += 1
            m += 1
            curNode = curNode.next

        while curNode is not None and n < to:
            m +=1
            newVector.append(curNode.data)

        return newVector

    def __iter__(self):
        return VectorIterator(self.Vectorhead)


class VectorNode:
    def __init__(self, data):
        self.data = data
        self.next = None

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
A
print(35 in A)

print(A)

