# Implementation of Deque ADT

class Deque:
    # Creates an Empty Deque
    def __init__(self):
        self._dequeHead = None
        self._dequeTail = self._dequeHead
        self._size = 0

    # Return the length of the Deque
    def __len__(self):
        return self._size

    # Determines if the Deque is Empty
    def isEmpty(self):
        return self._size == 0

    # Adds an item to the front of the deque
    def _frontEnqueue(self, item):
        newNode = DequeNode( item )
        if self._dequeHead is None:
            self._dequeHead = newNode
            self._dequeTail = self._dequeHead
        else:
            newNode.next = self._dequeHead
            self._dequeHead = newNode
        self._size +=1

    # Adds an item to the back of the deque
    def _backEnqueue(self, item):
        newNode = DequeNode( item )
        if self._dequeHead is None:
            self._dequeHead = newNode
            self._dequeTail = self._dequeHead

        else:
            self._dequeTail.next = newNode
            self._dequeTail = newNode
        self._size +=1

    # removes and return the item in front of the deque
    def _frontDequeue(self):
        assert not self.isEmpty(),\
            "Cannot dequeue from empty Deque"
        item = self._dequeHead.item
        self._dequeHead = self._dequeHead.next
        self._size -=1
        return item

    # Removes and return the item at the back of the deque
    def _backDequeue(self):
        assert not self.isEmpty(),\
            "Cannot dequeue from empty Deque"
        curNode = self._dequeHead

        while curNode is not None and curNode != self._dequeTail:
            preNode = curNode
            curNode = curNode.next

        if curNode is not None and curNode == self._dequeTail:
            item = curNode.item
            preNode.next = curNode.next
            self._dequeTail = preNode
            self._size -= 1
            return item

class DequeNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None


#TEST
test = Deque()
print(len(test))
test._frontEnqueue(0)
print(len(test))
test._frontEnqueue(4)
test._backEnqueue(9)
print(len(test))
print(test._frontDequeue())
print(len(test))