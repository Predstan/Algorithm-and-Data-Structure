
from stack import Stack


def isvalidSource(srcfile):
    s = Stack()
    for line in srcfile:
        for token in line:
            if token == "/":
                if s.isEmpty() or (s.peek() != "/"):
                    s.push(token)
                
                elif s.peek() == "/":
                    s.pop()
                    break
            elif token == '"' or token == "'":
                if s.isEmpty() or \
                    token == "'" and s.peek() != "'" or\
                    token == '"' and s.peek() != '"':
                    s.push(token)
               
                elif token == "'" and s.peek() == "'" or\
                    token == '"' and s.peek() == '"':
                        left = s.pop()
            elif token == "*":
                if s.peek() == "/" or s.peek() == "*":
                    s.push(token)

            elif token in "[{(":
                left = s.pop()
                if (left != "*" and s.peek() != "/") or \
                    (left != "'" and s.peek() != "'") or \
                    (left != '"' and s.peek() != '"'):
                    s.push(token)
                else:
                    s.push(left)

            elif token in "}])":
                if s.isEmpty():
                    return False  
            else:
                left = s.pop()
                if (token == "}" and left != "{") or\
                    (token == "]" and left != "[") or \
                    (token == ")" and left != "("):
                    return False

                    
            






