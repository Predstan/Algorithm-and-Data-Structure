from stack import Stack
import math

class PostFixCalculator:
    
    def __init__(self):
        self.operands = Stack()
        self.save = Stack()

    def value(self, value):
        self.operands.push(value)

    def result(self):
        if not self.operands.isEmpty():
            return self.operands.peek()

    def clear(self):
        self.operands = Stack()

    def clearLast(self):
        return self.operands.pop()

    def compute(self, op):
        if op in "*+-/":
            b = self.operands.pop()
            a = self.operands.pop()
        else:
            a = self.operands.pop()
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = a / b
        elif op == "**":
            result = a ** b
        elif op == "abs":
            result = abs(b)
        elif op == "sqrt":
            result = math.sqrt(a)
        elif op == "sin":
            result = math.sin(a)
        elif op == "cos":
            result = math.cos(a)
        elif op == "tan":
            result = math.cos(a)
        self.operands.push(result)

    def store(self):
        assert self.operands.isEmpty() is not True, \
            "No Value to Store"
        value = self.operands.pop()
        self.save.push(value)

    def recall(self):
        assert self.save.isEmpty() is not True, \
            "No Value to Recall"
        value = self.save.pop()
        self.operands.push(value)



