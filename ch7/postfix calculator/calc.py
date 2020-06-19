from postfix import PostFixCalculator

infile = open(filename, "r")
calc = PostFixCalculator()
for line in infile:
    if line[0].upper == "ENTER":
         calc.value = line[1]
    elif line[0].upper() == "MUL":
        calc.compute("*")

    elif line[0].upper() == "Add":
        calc.compute("+")

    elif line[0].upper() == "SUB":
        calc.compute("-")
    
    elif line[0].upper() == "DIV":
        calc.compute("/")

    elif line[0].upper() == "POW":
        calc.compute("**")
    
    elif line[0].upper() == "RESULT":
       print(calc.result())

    elif line[0].upper() == "CLR":
        calc.clear()
    
    elif line[0].upper() == "CLRLAST":
        calc.clearLast()

