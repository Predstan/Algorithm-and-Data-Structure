# Implements Map ADT Using Sorted List of Keys

class Map:
    def __init__(self):
        self.elements = list()

    # Returns the Length of the Keys
    def __len__(self):
        return len(self.elements)

    # Determines if Map contains a Key
    def __contains__(self, key):
        ndx = self.findPosition( key )
        return ndx < len(self) and self.elements[ndx].key == key

    # Remove a key in the Map
    def remove(self, key):
        ndx = self.findPosition( key )
        assert self.elements[ndx].key == key, "Key not Existing"
        self.elements.pop(ndx)


    # Returns the Value of a key in the Map
    def __getitem__(self, key):
        ndx = self.findPosition( key )
        assert self.elements[ndx].key == key, "Key not Existing"
        return self.elements[ndx].value

    # Sets the Value and key to the Map
    def __setitem__(self, key, value):
        ndx = self.findPosition( key ) # Returns the index of the Key
        
        # Determines if key already Exist
        if ndx < len(self) and self.elements[ndx].key == key:
            self.elements[ndx].value = value
        # Includes Key if not in Map
        else:
            entry = Mapentry(key, value)
            self.elements.insert(ndx, entry) 

    # Iterates over the key in the Map      
    def __iter__(self):
        return MapIterator(self.elements)

    # Returns the Keys and Values in the Map as a String
    def __str__(self):
        elements = []
        for element in self.elements:
            elements.append((str(element.key) + ' : ' + str(element.value)))
        return '{%s}' % str(elements).strip("[]").strip("()").strip("''").replace("'", "")

    # Helper to Find the proper position of a key
    def findPosition(self, key):
        low = 0
        high = len(self) - 1

        # Determines if Key is int or float
        # Returns Key as a String so that it can be easily Compared
        if isinstance(key, int) or isinstance(key, float):
            key = str(key)

        while low <= high:
            mid = (high + low)//2

            # Checks and compares key found and return the index
            if str(self.elements[mid].key) == key:
                return mid

            # Checks and compares key found is larger and move backward
            elif str(self.elements[mid].key) > key:
                high = mid - 1 
            # Checks and compares key found is smaller and move forward
            else:
                low = mid + 1

        return low



#  Storage Class for key and values
class Mapentry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

# Iterator for Map keys
class MapIterator:
    def __init__(self, thelist):
        self.thelist = thelist
        self.ndx = 0

    def __iter__(self):
        return self.thelist

    def __next__(self):
        if self.ndx < len(self.thelist):
            value = self.thelist[self.ndx].key
            self.ndx += 1
            return value

        raise StopIteration


# TEST
hey = Map()
hey["hi"] = 76
hey["hey"] = 80
hey["dog"] = 80
hey[30] = 80
hey.remove("dog")
print(hey["hey"])
print(hey["hi"])
print(len(hey))
print(hey)
hey[900] = "Cat"
hey["la"] = 80
print(hey)
print("la" in hey)
