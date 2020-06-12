#Implementation of Polynomial ADT using Python List
class polynomial:
    def __init__(self):
        self.poly = list()

    # Returns the highest degree of the polynomial
    def degree(self):
        if len(self.poly) is 0:
            return -1
        return self.poly[0].degree

    # Returns the Coefficient of a degree in the polynomial
    def __getitem__(self, degree):
        assert self.degree() >= degree, "Out of degree Range"
        ndx = self.findPosition(degree)
        return self.poly[ndx].coefficient

    # Appends a degree and coefficient of a polynomial
    def __setitem__(self, degree, coefficient):
        if coefficient != 0:
            ndx = self.findPosition( degree )
            newCof = polyterm(degree, coefficient)
            self.poly.insert(ndx, newCof)

    # Evaluate a polynomial Using a scaler Value
    def evaluate(self, scalar):
        result = 0
        for value in self.poly:
            result += value.coefficient * (scalar ** value.degree)

        return result

     # Adds Two Polynomial Expressions
    def __add__(self, polynomial_B):
        newPoly = polynomial()
        a = 0
        b = 0

        while a < len(self.poly) and b < len(polynomial_B.poly):
            if self.poly[a].degree == polynomial_B.poly[b].degree:
                coefficient = self.poly[a].coefficient + polynomial_B.poly[b].coefficient
                newPoly[self.poly[a].degree] = coefficient
                a += 1
                b += 1
            
            elif self.poly[a].degree > polynomial_B.poly[b].degree:
                newPoly[self.poly[a].degree] = self.poly[a].coefficient
                a += 1

            else:
                newPoly[polynomial_B.poly[b].degree] = polynomial_B.poly[b].coefficient
                b += 1

        while a < len(self.poly):
            newPoly[self.poly[a].degree] = self.poly[a].coefficient
            a += 1

        while b < len(polynomial_B.poly):
            newPoly[polynomial_B.poly[b].degree] = polynomial_B.poly[b].coefficient
            b += 1
        
        return newPoly

    # Subtract 2 Polynomials A and B
    def __sub__(self, polynomial_B):
        newPoly = polynomial()
        a = 0
        b = 0

        while a < len(self.poly) and b < len(polynomial_B.poly):
            if self.poly[a].degree == polynomial_B.poly[b].degree:
                coefficient = self.poly[a].coefficient - polynomial_B.poly[b].coefficient
                newPoly[self.poly[a].degree] = coefficient
                a += 1
                b += 1
            
            elif self.poly[a].degree > polynomial_B.poly[b].degree:
                newPoly[self.poly[a].degree] = self.poly[a].coefficient
                a += 1

            else:
                newPoly[polynomial_B.poly[b].degree] = -polynomial_B.poly[b].coefficient
                b += 1

        while a < len(self.poly):
            newPoly[self.poly[a].degree] = self.poly[a].coefficient
            a += 1

        while b < len(polynomial_B.poly):
            newPoly[polynomial_B.poly[b].degree] = -polynomial_B.poly[b].coefficient
            b += 1

    # Retuns the Multiplication of Two Polynomials 
    def __mul__(self, polynomial_B):
        newPoly = polynomial()
        

        for value in self.poly:
            poly_2 = polynomial()
            for value_b in polynomial_B.poly:
                degree = value.degree + value_b.degree
                coefficient = value.coefficient * value_b.coefficient
                poly_2[degree] = coefficient

            newPoly += poly_2

        return newPoly



    # Helper Method to sort and search the position of an entry into the Polynomial
    def findPosition(self, degree):
        low = 0
        high = len(self.poly)-1

        while low <= high:
            mid = (high +low) //2

            if self.poly[mid].degree == degree:
                return mid

            elif self.poly[mid].degree > degree:
                low = mid + 1

            else:
                high = mid - 1

        return low
    def print(self):
        for value in self.poly:
            print(value.degree, value.coefficient)

class polyterm:
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient



# TEST    
A = polynomial()
A[1] = 3
A[2] = 5
A[0] = -10
B = polynomial()
B[3] = 2
B[2] = 4
B[0] = 3

print(A.degree())
print(B.degree())
C = A+B
print(C.degree())
D = A * B
print(D.degree())
E = D.evaluate(3)
print(E)
print(A.evaluate(0))

D.print()