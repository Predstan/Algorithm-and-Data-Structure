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
            print(curNode.next.data)
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
deleteNode(head, 4)
transversal(head)
print("\n")
prenode = None
curNode = head
while curNode is not None and curNode.data != 4:
    prenode = curNode
    curNode = curNode.next
if curNode is not None:
    if 4 == head.data:
        head = curNode.next
        print(head.data)

    else:
        prenode.next = curNode.next
transversal(head)


print(1 == 1.0)
