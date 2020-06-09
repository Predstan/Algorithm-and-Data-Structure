# Implementation of Polynomial ADT using LinkedList
class polynomial:
    # Creates a polynomial that accept an optional degree and a coefficient
    def __init__(self, degree = None, coefficient = None):
        if degree is None:
            self.polyhead = degree
        else:
            self.polyhead = polyNode(degree, coefficient)
        self.polytail = self.polyhead

    # Returns the highest degree of the polynomial
    def degree(self):
        if self.polyhead is None:
            return -1
        else:
            return self.polyhead.degree

    # Returns the Coefficient of a degree in the polynomial
    def __getitem__(self, degree):
        curNode = self.polyhead

        while curNode is not None and curNode.degree > degree:
            curNode = curNode.next
        
        if curNode is None or curNode.degree != degree:
            return 0

        else:
            return curNode.coefficient

    # Appends a degree and coefficient of a polynomial
    def appendTerm(self, degree, coefficient):
        curNode = self.polyhead
        preNode = None
        if coefficient != 0:
            while curNode is not None and curNode.degree > degree:
                preNode = curNode
                curNode = curNode.next
        
            newNode = polyNode(degree, coefficient)
            newNode.next = curNode
            if curNode == self.polyhead:
                    self.polyhead = newNode
            else:
                preNode.next = newNode
        

    # Evaluate a polynomial Using a scaler Value
    def evaluate(self, scalar):
        assert self.degree() >= 0, " Cannot Evaluate Empty Polynomial"
        curNode = self.polyhead
        result = 0
        while curNode is not None:

            result += curNode.coefficient * (scalar ** curNode.degree)
            curNode = curNode.next

        return result


    # Adds Two Polynomial Expressions
    def __add__(self, polynomial_B):
        # Creates a New Polynomial for the Resulting Polynomial
        newPoly = polynomial()
        curNodeA = self.polyhead
        curNodeB = polynomial_B.polyhead
        # Iteartes Both Polynomials
        while curNodeA is not None and curNodeB is not None:
            # Determines if they have the same degree and 
            # Append the result of addition to the new Polynomial
            if curNodeA.degree == curNodeB.degree:
                add = curNodeA.coefficient + curNodeB.coefficient
                newPoly.appendTerm(curNodeA.degree, add)
                curNodeA = curNodeA.next
                curNodeB = curNodeB.next
            # Determines if degree of polynomial A is Larger
            elif curNodeA.degree > curNodeB.degree:
                newPoly.appendTerm(curNodeA.degree, curNodeA.coefficient)
                curNodeA = curNodeA.next
            # Determines if degree of polynomial B is Larger
            else:
                newPoly.appendTerm(curNodeB.degree, curNodeB.coefficient)
                curNodeB = curNodeB.next
        # Iterates Over the rest of polynomial B if there are still Values
        while curNodeB is not None:
            newPoly.appendTerm(curNodeB.degree, curNodeB.coefficient)
            curNodeB = curNodeB.next
        # Iterates Over the rest of Polynomial A if there are still Values
        while curNodeA is not None:
            newPoly.appendTerm(curNodeA.degree, curNodeA.coefficient)
            curNodeA = curNodeA.next
        
        return newPoly

    def __sub__(self, polynomial_B):
        # Creates a New Polynomial for the Resulting Polynomial
        newPoly = polynomial()
        curNodeA = self.polyhead
        curNodeB = polynomial_B.polyhead
        # Iteartes Both Polynomials
        while curNodeA is not None and curNodeB is not None:
            # Determines if they have the same degree and 
            # Append the result of subtraction to the new Polynomial
            if curNodeA.degree == curNodeB.degree:
                add = curNodeA.coefficient - curNodeB.coefficient
                newPoly.appendTerm(curNodeA.degree, add)
                curNodeA = curNodeA.next
                curNodeB = curNodeB.next
            # Determines if degree of polynomial A is Larger 
            elif curNodeA.degree > curNodeB.degree:
                newPoly.appendTerm(curNodeA.degree, curNodeA.coefficient)
                curNodeA = curNodeA.next
            # Determines if degree of polynomial B is Larger
            else:
                newPoly.appendTerm(curNodeB.degree, -curNodeB.coefficient)
                curNodeB = curNodeB.next
        # Iterates Over the rest of polynomial B if there are still Values
        while curNodeB is not None:
            newPoly.appendTerm(curNodeB.degree, -curNodeB.coefficient)
            curNodeB = curNodeB.next
        # Iterates Over the rest of Polynomial A if there are still Values
        while curNodeA is not None:
            newPoly.appendTerm(curNodeA.degree, curNodeA.coefficient)
            curNodeA = curNodeA.next
        
        return newPoly

    # Returns the result of Two Polynomials 
    def __mul__(self, polynomial_B):

        assert self.degree() >= 0 and polynomial_B.degree() >=0,\
             " Cannot Multiply Empty Polynomials"
        # Creates a new Polynomial to store the result
        newPoly = polynomial()
        curNodeA = self.polyhead
        curNodeB = polynomial_B.polyhead
        # Iterates over Polynomial A and pick the individual Values
        while curNodeA is not None:
            # Creates another Polynomial for the resulting Polynomial 
            # that is obtained from the Multiplication of individual
            # Values of A
            poly_2 = polynomial()
            NextNode = curNodeB
            # Iterate over Polynomial B and multiply the values
            # By each of Polynomial A
            while NextNode is not None:
                degree = curNodeA.degree + NextNode.degree
                coefficient = curNodeA.coefficient * NextNode.coefficient
                poly_2.appendTerm(degree, coefficient)
                NextNode = NextNode.next
            # Add the resulting polynomials
            newPoly += poly_2
            curNodeA = curNodeA.next

        return newPoly


# Storage Class For the Linedlist and the coefficient and degree
# of a Polynomial           
class polyNode(object):

    def __init__(self, degree, coefficient):
        self.coefficient = coefficient
        self.degree = degree
        self.next = None
        

# TEST    
A = polynomial()
A.appendTerm(1, 3)
A.appendTerm(2, 5)
A.appendTerm(0, -10)
B = polynomial()
B.appendTerm(3, 2)
B.appendTerm(2, 4)
B.appendTerm(0, 3)

C = B - A
print(C.degree())
D = A * B
print(D.degree())
E = D.evaluate(3)
print(E)
print(A[1])
print(C[0])



