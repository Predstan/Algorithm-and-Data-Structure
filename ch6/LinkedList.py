class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

def transversal( head ):
    curNode = head
    while curNode is not None:
        print (curNode.data)
        curNode = curNode.next

    return "end"

def unorderedSearch(head, target):
    curNode = head
    n = 0
    while curNode is not None and curNode.data != target:
        n +=1
        curNode = curNode.next

    return curNode is not None, n


# Given the head reference, remove a target from the linked list
def deleteNode(head, target):
    prenode = None
    curNode = head
    while curNode is not None and curNode.data != target:
        prenode = curNode
        curNode = curNode.next

    if curNode is not None:
        if target == head.data:
            head = curNode.next

        else:
            prenode.next = curNode.next
    return head


head = LinkedList("a")
head.next = LinkedList("g")
head.next.next = LinkedList(0)
NewNode = LinkedList(4)
NewNode.next = head
head = NewNode

transversal(head)
print(unorderedSearch(head, 4))
print("\n")
transversal(deleteNode(head, "a"))

# Add a Node when Head and Tail is referenced
def add(head, tail, target):
    NewNode = LinkedList( target )
    if head is None:
        head = NewNode
    else:
        tail.next = NewNode
    tail = NewNode

# Add with only head referenced
def addUnsorted(head, target):
    NewNode = LinkedList(target)
    if head is None:
        NewNode = head
    else:
        NewNode.next = head
        head = NewNode

# Remove a Node when Tail and Head is Given
def remove(head, tail, target):
    prenode = None
    curNode = head
    while curNode is not None and curNode.data != target:
        prenode = curNode
        curNode = curNode.next

    if curNode is not None:
        if curNode == head:
            head = curNode.next
        if curNode == tail:
            tail = prenode
        else:
            prenode.next = curNode.next

# Search Sorted LinkedList
def SearchSorted(head, target):
    curNode = head
    while curNode is not None and curNode.data < target:
        if curNode.data == target:
            return True

        else:
            curNode = curNode.next
    return False
# Add in a Sorted Linked List
def addSorted(head, target):
    preNode = None
    curNode = head
    while curNode is not None and curNode.data < target:
        preNode = curNode
        curNode = curNode.next
    
    NewNode = LinkedList( target )
    NewNode.next = curNode
    if curNode is head:
        head = NewNode
    else:
        preNode.next = NewNode

    return head

def deleteSorted(head, target):
    preNode = None
    curNode = head

    while curNode is not None and curNode.data < target:
        preNode = curNode
        curNode = curNode.next

    if curNode is not None:
        if head.data == target:
            head = curNode.next
        elif curNode.data == target:
            preNode.next = curNode.next

def removeall(head):
    curNode = head
    preNode = None
    while curNode is not None:
        preNode = curNode.next
        curNode = preNode

    return curNode

def splitInHalf(head):
    n = length(head)
    curNode = head
    n = n//2
    m = 0
    while m != n :
        m += 1
        curNode = curNode.next

    return curNode

def length(head):
    curNode = head
    n = 0
    if curNode is None:
        return None 

    while curNode is not None:
        n +=1
        curNode = curNode.next

    return n
    
