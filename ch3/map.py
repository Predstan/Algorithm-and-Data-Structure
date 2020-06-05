from Array import Array
# Implementation of Mapping ADT using a single list

class Map:
    # Creates an Instance of an empty Map
    def __init__(self):
        self.map = list()

    # Returns the Number of key in the Map
    def __len__(self):
        return len(self.map)

    # Returns True if key is contained in the Map
    def __contains__(self, key):
        ndx = self.findPosition( key )
        return ndx is not None

    # Adds new key and Add Value if key not already in the Map
    # Otherwise, Adds replaces the value of the key existing
    def add(self, key, value):
        ndx = self.findPosition( key )
        if ndx is not None: # If Key is in Map
            self.map[ndx].value = value # Replaces Value
            return False
        else: # Otherwise key not in Map
            entry = MapEntry(key, value) 
            self.map.append(entry)
            return True

    # Returns the Value of Key if Key is in the Map
    def valueOf(self, key): 
        ndx = self.findPosition(key)
        if ndx is not None:
            return self.map[ndx].value
        
        return "Invalid Key"

    # Removes Key in map is key is present in Map
    def remove(self, key):
        ndx = self.findPosition( key )
        assert ndx is not None, "Invalid Key"
        self.map.remove(self.map[ndx])

    # Iterates over Keys in the Map
    def __iter__(self):
        return mapIterator(self.map)

    # Returns the Position of a key in the Map,
    # Otherwise, returms None
    def findPosition(self, key):
        for i in range(len(self.map)):
            if self.map[i].key == key:
                return i
        return None

    # Sets the value of a particular key
    def __setitem__(self, key, value):
        ndx = self.findPosition( key )
        if ndx is not None: # If Key is in Map
            self.map[ndx].value = value # Replaces Value
            return False
        else: # Otherwise key not in Map
            entry = MapEntry(key, value) 
            self.map.append(entry)
            return True

    # Returns the value of a key
    def __getitem__(self, key):
        ndx = self.findPosition(key)
        if ndx is not None:
            return self.map[ndx].value
        
        return "Invalid Key"

    # Returns the Array of keys
    def keyArray(self):
        keyArray = Array(len(self))
        for i in range(len(self)):
            keyArray[i] = self.map[i].key


# Class for Key Value parts
class MapEntry:

    def __init__(self, key, value):
        self.value = value
        self.key = key
 

class mapIterator:

    def __init__(self, thelist):
        self.thelist = thelist
        self.ndx = 0


    def __iter__(self):
        return self.thelist


    def __next__(self):
        if self.ndx < len(self.thelist):
            key = self.thelist[self.ndx].key
            self.ndx += 1
            return key

        raise StopIteration


hey = Map()
hey.add("hey", 78)
hey.add("hi", 80)

print(hey["hey"])
