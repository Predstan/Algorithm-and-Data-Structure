# Implementation of Bounded Queue ADT

from Queue import queue
from Array import Array


class Bpriority:
    # Create and initialize the number of priorities in the Queue
    def __init__(self, numlevels):
        self.Bounded = Array(numlevels)
        self.size = 0
        
        for i in range(numlevels):
            self.Bounded[i] = queue()

    # Returns the length of the items in the queue
    def __len__(self):
        return self.size

    # Determines if Queue is Empty
    def isEmpty(self):
        return self.size == 0

    # Enqueue an item according to priority
    def enqueue(self, item, priority):
        assert priority < len(self.Bounded),\
            "Priority not available"

        self.Bounded[priority].enqueue(item)
        self.size += 1

    # Returns and Remove an item with higher priority from the Queue
    def dequeue(self):
        assert not self.isEmpty(), \
            "Queue is empty"

        for i in range(len(self.Bounded)):
            if not self.Bounded[i].isEmpty():
                self.size -= 1
                return self.Bounded[i].dequeue()




Q = Bpriority( 6 )
Q.enqueue( "purple", 5 )
Q.enqueue( "black", 1 )
Q.enqueue( "orange", 3 )
Q.enqueue( "white", 0 )
Q.enqueue( "green", 1 )
Q.enqueue( "yellow", 5 )

while not Q.isEmpty() :
    item = Q.dequeue()
    print( item )

    