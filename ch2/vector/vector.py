# implements the Vector ADT 1-d Array 

#Imports 1-D Array Class
from Array import Array


class vector:

    # Creates the Vector Array intialized to 2
    def __init__(self):
        self.vector = Array(2)

    # Returns the length of values in the Vector
    def __len__(self):
        j=0
        # Iterates over the values in the vector
        for i in range(self.vector.size):
            # Checks for values in the Vector
            if self[i] != None:
                j+=1
        return j

    # Checks if Vector contains the Requested Value
    def contains(self, item):
       for i in range(self.vector.size):
           return self.vector[i] == item

    # Returns the Value in the index 
    def __getitem__(self, ndx):
        return self.vector[ndx]

    # Sets the value in the index
    def __setitem__(self, ndx, value):
         self.vector[ndx] = value
                
    # Appends Value to the end of the list
    def append(self, item):
        j = 0
        # iterates over the list of items
        for i in range(len(self.vector)):
            # Checks if there is an item in the index and append item if there is None
            if self[i] == None:
                self[i] = item
                break
            # Continues loop of there is an item in the index
            else:
                j +=1
                continue

        # Checks if this is the end of the list 
        if j == len(self):
            tmp = self.vector
            # Expands the list to creates more storage for item
            self.vector = Array(len(self)+1)
            # append items in the new list
            for i in range(len(tmp)):
                self[i] = tmp[i]
            self.append(item)

    # Inserts Value to the particular index
    def insert(self, ndx, item):
        tmp = self.vector
        # Breaks the list and expands
        self.vector = Array(len(self)+1)
        
        # Assign the items before the index
        for i in range(0, ndx):
            self[i] = tmp[i]
        
        # Assign the item to the index
        self[ndx] = item

        # Shifts the item down for more space
        for i in range(ndx, len(tmp)):
            self.append(tmp[i])

    # Removes and return the item at an index
    def remove(self, ndx):
        item = self.vector[ndx]
        tmp = self.vector

        # Breaks the list for shifting to close the gap
        self.vector = Array(len(self)-1)

        # inserts the item before the index
        for i in range(0, ndx):
            self[i] = tmp[i]
        
        # Removes the item at the index
        for i in range(ndx+1, len(tmp)):
            self[i-1] = tmp[i]
        return item

    # Returns the index of an item if available in the list
    def indexOf(self, item):
        for i in range(len(self)):
            if self[i] == item:
                return i
        return "Item not in list"
    
    # Extends the List by appending another list at the end
    def extend(self, otherVector):
        a = self.vector
        self.vector = Array(len(self)+len(otherVector))
        for i in range(len(a)):
            self.append(a[i])
        for i in range(len(otherVector)):
            self.append(otherVector[i])

    # Creates and returns a SubVector from the List
    def subVector(self, From, to):
        assert to <= len(self), "Out of Range"
        subVector = vector()
        for i in range(From, to+1):
            subVector.append(self[i])
        return subVector

    # Iterates over the items in the List
    def __iter__(self):
        return iter(self.vector)
        




    


daf = vector()
print(len(daf))
daf.append(9)
print(len(daf))
daf.append(5)
print(len(daf))
daf.append(6)
print(len(daf))
print(len(daf))
print("\n")

print("\n")

b = vector()
b.append(8)
b.append(9)
b.append(7)
b.insert(1, 6)
b.remove(1)
daf.extend(b)

print(daf)
print("\n")
sub = daf.subVector(1, 5)

print("\n")
for i in range(len(b)):
    print(next(iter(b)))














        
    

        