# iMPLEMENTATION OF QUEUE USING CIRCULAR ARRAY

from Array import Array

class Queue:
    def __init__(self, numelements):
        self.elements = Array(numelements)
        self.counts = 0
        self.front = 0
        self.back = self.front

    # Determines if queue is empty
    def isEmpty(self):
        return self.counts == 0

    # Returns the length of items in the Queue
    def __len__(self):
        return self.counts

    # Adds an item to the back of the queue
    def enqueue(self, item):
        assert self.counts != len(self.elements),\
            " Queue is Full"
        if self.counts == 0:
            self.elements[self.counts] = item
            self.front = 0
            self.back = 0
            self.counts += 1

        else:
            self.back += 1
            self.front = (self.front + 1) % len(self.elements)
            self.elements[self.back] = item
            self.counts += 1
        

    # Removes an item at the front of the queue
    def dequeue(self):
        assert not self.isEmpty(), \
            "Queue is Empty"

        
    
        item = self.elements[self.front]
        self.elements[self.front] = None
        self.front = (self.front + 1) % len(self.elements)
        self.counts -= 1
        return item
        

# TEST
hey = Queue(5)
hey.enqueue(9)
hey.enqueue(8)
hey.enqueue(7)
hey.enqueue(0)
hey.enqueue(9)

print(len(hey))
print(hey.dequeue())
print(len(hey))
print(hey.dequeue())
print(hey.dequeue())
print(hey.dequeue())
print(len(hey))
hey.enqueue(8)
print(len(hey))
print(hey.dequeue())
print(hey.dequeue())
print(len(hey))
print(hey.dequeue())