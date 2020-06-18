# Linked List Implementation of Stack ADT
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    # determines if the Stack is empty
    def isEmpty(self):
        return self.head == None

    # Returns the number of elements in the Stack
    def length(self):
        return self.size

    # Removes and returns the Last in element
    def pop(self):
        assert self.isEmpty() is not True,\
            "Stack is empty"
        item = self.head.item
        self.head = self.head.next
        self.size -= 1
        return item

    # Check the Last element into the Stack
    def peek(self):
        assert self.isEmpty() is not False,\
            "Stack is empty"
        return self.head.item

    # Push an element into the Stack
    def push(self, item):
        self.head = StackNode( item, self.head )
        self.size += 1

class StackNode(object):
    def __init__(self, item, base):
        self.item = item
        self.next = base
