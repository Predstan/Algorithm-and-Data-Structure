class bag():
    def __init__(self):
        self.val = list()

    def length(self):
        return len(self.val)

    def contains(self, value):
        if value in self.val:
            return True
        else:
            return False

    def add(self, value):
        return self.val.append(value)

    def extend(self, newlist):
        return self.val.extend(newlist.val)

    def remove(self, value):
        assert value in self.val, "The item is not available"
        idx = self.val.index(value)
        return self.val.pop(idx)

    def __iter__(self):
        return BagIterator(self.val)


class BagIterator:

    def __init__(self, thelist):
        self.list = thelist
        self.ndx = 0


    def __iter__(self):
        return self.list


    def __next__(self):
        if self.ndx < len(self.list):
            new = self.list[self.ndx]
            self.ndx += 1
            return new

        raise StopIteration
           
        



