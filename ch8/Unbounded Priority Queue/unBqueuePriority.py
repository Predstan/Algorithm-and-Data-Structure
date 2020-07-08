# Implementation of Unbounded Priority Queue Using Python List
class PriorityQueue:
    # Creates an instance of of the queue element
    # Accepts the number of levels from 0
    def __init__(self, numlevels):
        self.elements = list()
        self.highest = numlevels

    # Determines if the queue is empty
    def isEmpty(self):
        return len(self.elements) == 0

    # Returns the length of items in the queue
    def __len__(self):
        return len(self.elements)

    # Adds an item to the queue with priority level
    def enqueue(self, item, priority):
        assert priority <= self.highest, \
            "Priority not in range"
        item = unBoundedpriorityQueue(priority, item)
        self.elements.append(item)

    # Removes and return an Item using FIFO(First in First Out)
    def dequeue(self):
        assert not self.isEmpty(),\
            "Queue is Empty"
        highest = self.highest
        index = 0
        for i in range(len(self)):
            if self.elements[i].priority < highest:
                highest = self.elements[i].priority
                index = i
        item = self.elements.pop(index)
        return item.item


# Storage for item and priority
class unBoundedpriorityQueue:
    def __init__(self, priority, item):
        self.priority = priority
        self.item = item

    

Q = PriorityQueue( 6 )
Q.enqueue( "purple", 5 )
Q.enqueue( "black", 1 )
Q.enqueue( "orange", 3 )
Q.enqueue( "white", 0 )
Q.enqueue( "green", 1 )
Q.enqueue( "yellow", 5 )

while not Q.isEmpty() :
    item = Q.dequeue()
    print( item )