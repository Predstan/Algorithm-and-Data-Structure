# Implementation of Priority Queue Using Sorted LinkedList

class priorityQueue:
    # Create an Instance of the Queue
    def __init__(self):
        self.queuehead = None
        self.size = 0
        

    # Rerturn the Length of the Queue
    def __len__(self):
        return self.size

    # Detyermines if Queue is Empty
    def isEmpty(self):
        return self.size == 0

    # Adds an Item to the Queue with the Priority
    def enqueue(self, item, priority):
        assert priority >= 0,\
            "Priority must be within Valid Range"
        curNode = self.queuehead
        preNode =   None
        newNode = queue(item, priority)

        while curNode is not None and curNode.priority <= priority:
            preNode = curNode
            curNode = curNode.next


        else:
            if self.queuehead == None:
                self.queuehead = newNode 

            elif curNode == self.queuehead:
                newNode.next = curNode
                self.queuehead = newNode
            else:
                newNode.next = curNode
                preNode.next = newNode

        self.size += 1

    # Remove and Return an Item using FIFO (First in First Out)
    def dequeue(self):
        assert not self.isEmpty(), \
            "Cannot dequeue from an empty List"
        item = self.queuehead.item
        self.queuehead = self.queuehead.next
        self.size -= 1
        return item


# LinkedList and Storage Class
class queue(object):
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
        self.next = None



