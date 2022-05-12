from lark import Lark
from functools import reduce

# Notes about grammar:
# To start, the user can enter either a string or an exp. The string must be all
# uppercase characters. If they enter an expression, it will be an s_exp, meaning
# it must have the parentheses. In that case, the parenthese will be surrounding
# one or more atoms, which are var(the function), num, and str. The var must
# consists of all lowercase letters to differentiate it from str. The var can
# also be some basic arithmetic symbols, with the exception of division. Additionally, defining variables via def considers the variable to be be an str. This means that any defined variable must follow the rules of a string, meaning it must consist of one or more capital letters.
my_grammar = """
?start: exp | str
?exp: s_exp | atom
s_exp: "(" exp+ ")"
?atom: var | num | str
str: /[A-Z]+/
num: NUMBER
?var: /[a-z]+/ | /[+]/ | /[-]/ | /[*]/ | /[%]/
%import common.NUMBER
%import common.WS
%ignore WS
"""

varsDict = {}

def apply(f, args):
    if f == 'add' or f == '+':
        return reduce((lambda x, y: x+y), args)

    elif f == 'mul' or f == '*':
        return reduce((lambda x, y: x*y), args)

    elif f == 'div':
        return reduce((lambda x, y: x/y), args)

    elif f == 'mod' or f == '%':
        return reduce((lambda x, y: x%y), args)

    elif f == 'sub' or f == '-':
        return reduce((lambda x, y: x-y), args)

    elif f == 'def':
        defList = list(args)
        varsDict[defList[0]] = defList[1]
        print(varsDict[defList[0]])
        return None

    elif f == 'cons':
        # Store the list of arguments after the map
        consList = list(args)

        # Build a cons cell structure for each cons call
        consString = "'" + "(" + str(consList[0]) + "." + str(consList[1]) + ")"

        # Replace all the periods with spaces
        replacePeriods = consString.replace(".", " ")

        # Code to replace the extra parentheses when a recursive cons call occurs
        replaceParens = ""
        index = 1
        for i in replacePeriods:
            if i == "(" or i == ")":
                if index == 2 or index == (len(replacePeriods)):
                    replaceParens = replaceParens + i
            else:
                replaceParens = replaceParens + i
            index += 1

        # Code to replace the extra ' symbols when a recursive cons call occurs
        replaceSymbol = ""
        index = 1
        for i in replaceParens:
            if i == "'":
                if index == 1:
                    replaceSymbol = replaceSymbol + i
            else:
                replaceSymbol = replaceSymbol + i
            index +=1

        # Return the cons cell structure
        return replaceSymbol

    elif f == 'car':
        # Store the list of arguments
        carList = list(args)

        # Build the car string until the first space occurs, indicating the end of the first value
        carString = ""
        i = 0
        while 1:
            if carList[0][i] != " ":
                carString = carString + carList[0][i]
            else:
                break
            i += 1

        # Return the car
        return carString[2:]

    elif f == 'cdr':
        # Store the list of arguments
        cdrList = list(args)
        cdrString = ""

        # Find the index where the first space occurs. That indicates the point at which the cdr string should start
        spaceIndex = 0
        while 1:
            if cdrList[0][spaceIndex] == " ":
                break
            spaceIndex += 1

        # Add all values in the cons cell structure after the space to the cdr
        while spaceIndex != len(cdrList[0]) - 1:
            cdrString = cdrString + cdrList[0][spaceIndex]
            spaceIndex += 1

        #Return the cdr
        return cdrString

    elif f == 'list':
        #Store the list arguments
        listStructure = list(args)

        # Build the list structure
        listString = "'("
        i = 0
        for d in listStructure:
            listString = listString  + str(d)
            if i != len(listStructure) - 1:
                listString = listString + " "
            i += 1
        listString = listString + ")"

        # Remove the ' symbols after each recursive call
        finalList = ""
        i = 0
        for d in listString:
            if d == "'":
                if i == 0:
                    finalList = finalList + d
            else:
                finalList = finalList + d
            i +=1
        # Return final list
        return finalList

    # If the command is not recognized, raise an error
    else:
        raise SyntaxError('unknown function')

def eval_tree(t):
    if t.data == 's_exp':
        func = t.children[0]
        args = map(eval_tree, t.children[1:])
        return apply(func, args)
    elif t.data == 'num':
        return int(t.children[0])
    elif t.data == 'str':
        return str(t.children[0])
    else:
        raise SyntaxError('unrecognized tree')

parser = Lark(my_grammar)

program = input("Enter your single line program: ")

parse_tree = parser.parse(program)

print(parse_tree.pretty())

print(eval_tree(parse_tree))
