#Implementation of MultiArray Using 1-D Array
from Array import Array

# Creates a multi dimentional Array
class MultiArray:

    def __init__(self, *dimensions):
        assert len(dimensions) > 1, "The Array Must be greater than 1"
        # The tuple contains the sizes of each dimension
        self.dims = dimensions

        # The total Number of element in the array
        size = 1
        for d in dimensions:
            assert d > 0, "Dimensions must be greater than 0"
            size *= d

        # Creates 1-D Array to store the elements 
        self.elements = Array(size)

        # Creates 1-D Array to store the factors of the Array
        # This is denoted from the calculation fn = 1
        self.factors = Array(len(dimensions))

        # Computes and stores the factors in the factors array
        self.computeFactors()

    # Returns the number of Dimensions in the Array
    def numDims(self):
        return len(self.dims)

    # Returns the length of the given dimension
    def length(self, dim):
        assert dim >= 1 and dim < len(self.dims), " Dimesion out of Range"
        return self.dims[dim - 1]

    # Sets all elements in the Array to a value
    def clear(self, value):
        self.elements.clear(value)

    # Returns the element in the given dimension(i_!, i_2 ... i_n)
    # where number I is the number of dimensions in the Multi Array
    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == self.numDims(), "Invalid number of Array Subscript"
        index = self.computeIndex(ndxTuple)
        assert index is not None, "Array Subscript out of Range"
        return self.elements[index]
    
    # Sets the value in a partucular index
    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == self.numDims(), "Invalid number of Array Subscript"
        index = self.computeIndex(ndxTuple)
        assert index is not None, "Array Subscript out of Range"
        self.elements[index] = value
        
    # Computes the offset for an element at a particular index
    def computeIndex(self, idx):
        offset = 0
        for j in len(idx):
            if idx[j] < 0 or idx[j] > self.numDims():
                return None
            else:
                offset += idx[j] * self.factors[j]
        return offset

    # Computes the vactor values
    def computeFactors(self):
        dim = self.dims[1:]
        sort = 1
        for i in range(len(self.factors)):
            for value in dim:
                sort *= value
            self.factors[i] = sort
            dim = dim[1:]
            sort = 1



hey = MultiArray(4, 5, 6, 7)
print(hey.length(1))