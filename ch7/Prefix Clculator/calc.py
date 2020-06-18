# Implementing Prefix Calculator using 2 stacks
from stack import Stack


def prefixCalc(srcfile):
    # Create a Stack for number storage
    num = Stack()
    # Create a stack for operands Storage
    ath = Stack()
    # Read the txt File by line
    for line in srcfile:
        # Reads each value in the line
        for token in line:
            # Push Operands into Stack
            if token in "+-*/":
                ath.push(token)
            # Push value into stack
            elif token not in "+-*/":
                if num.isEmpty():
                    num.push(token)
                else:
                    art = ath.pop()
                    a = num.pop()
                    b = token
                    if art == "+":
                        result = float(a) + float(b)
                    elif art == "*":
                        result = float(a) * float(b)
                    elif art == "-":
                        result = float(a) - float(b)
                    elif art == "/":
                        result == float(a) / float(b)
                    num.push(result)
    return num.pop()

infile = open("untitled.txt", "r")
answer = prefixCalc(infile)
print(answer)
