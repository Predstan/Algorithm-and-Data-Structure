# Todo List ADT using Priority Queue

from PriorityQueueLinkedList import priorityQueue

class TodoList:
    # Create an empty Todo LIST
    def __init__(self):
        self.List = priorityQueue()

    # Return length of Activities
    def __len__(self):
        return len(self.List)

    # Add an activity
    def add(self, activity, priority):
        self.List.enqueue(activity, priority)

    # Perform and display an activity
    def performActivity(self):
        activity = self.List.dequeue()
        return activity


# TEST
todo = TodoList()
todo.add("Work", 0)
todo.add("Run", 2)
todo.add("Read", 1)
todo.add("eat", 4)
todo.add("bath", 3)

for i in range(len(todo)):
    print(todo.performActivity())