class Bag:
    # Construct an Empty Bag
    def __init__(self):
        self.head = None
        self.next = None
        self.size = 0

    # Returns the length of the Bag
    def __len__(self):
        return self.size

    # Determines if the Bag contains an Item
    def __contains__(self, item):
        curNode = self.head
        while curNode is not None and curNode.item != item:
            curNode = curNode.next

        return curNode is not None

    # Add an item to the Bag
    def add(self, item):
        newNode = BagListNode( item )
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    # Remove an Item from the Bag
    def remove(self, item):
        preNode = None
        curNode = self.head
        while curNode is not None and curNode.item != item:
            preNode = curNode
            curNode = curNode.next

        # Assert Item in Bag to be Removed
        assert curNode is not None, "Item not in Bag"

        # Remove the Link between Item to drop Item
        
        if curNode == self.head:
            self.head = curNode.next
        else:
            preNode.next = curNode.next

        self.size -=1
        return curNode.item

    # Returns an Iteration for transversing the Items in the Bag
    def __iter__(self):
        return BagIterator(self.head)

# Defines a private storage class for creating list nodes
class BagListNode( object ):

    def __init__(self, item):
        self.item = item
        self.next = None

# Bag Iterator Storage to keep track of Items
class BagIterator:

    def __init__(self, head):
        self.curNode = head
        self.ndx = 0


    def __iter__(self):
        return self.curNode

    def __next__(self):

        if self.curNode is not None:
            item = self.curNode.item
            self.curNode = self.curNode.next
            return item

        raise StopIteration

# TEST
yat = Bag()
print(len(yat))
yat.add(6)
yat.add(9)
yat.add(5)
yat.add(15)
yat.remove(5)
print(len(yat))
print(15 in yat)
for i in yat:
    print(i)