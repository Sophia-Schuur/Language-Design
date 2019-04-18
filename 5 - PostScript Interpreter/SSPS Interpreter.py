# Sophia Schuur 11519303
# 4/13/2019
# an interpreter for a simple scoped postScript 

# Windows intended.

import re
scope = ""
#------------------------- opstack operators -------------------------------------
opstack = [] 


def opPop():
    if (len(opstack) > 0):
        return opstack.pop()
    else:
        print("[!] - Operator stack empty")

def opPush(value):
    opstack.append(value)

#-------------------------- dict operators ------------------------------------- 
dictstack = []  

def dictPop():
    if (len(dictstack) > 0):
        return dictstack.pop()
    else:
        print("[!] - Dictionary stack empty")

def dictPush(d):
    dictstack.append(d)

def define(name, value):
    if(len(dictstack) == 0):
        d = dict()
        d[name] = value
        dictPush((0, d))    # "static link"?? "Activation record"??? oh well its just gonna be 0 for now.

    else:   
        (dictstack[-1][1])[name] = value


def lookup(name, scope):
    name = '/' + name  
    if (scope == 'static'):
        return staticLookup(list(dictstack), name, (len(dictstack) - 1))

    elif (scope == 'dynamic'):
        for item in reversed(dictstack):
            (index, d) = item

            if (name in d):
                return (index, d.get(name))
        else:
            return None

def staticLookup(d, name, index):
    if (name in dictstack[index][1]):
        return (index, dictstack[index][1][name])

    elif (index == dictstack[index][0]):
        return None

    else:
        next, _ = dictstack[index]
        _ = d.pop(index)
        return staticLookup(d, name, next)

#--------------------Arithmetic and comparison operators--------------------------------------------
def add():
    if len(opstack) >= 2:
        if (type(opstack[-1]) is int or float) and (type(opstack[-2]) is int or float):
            op1 = opPop()
            op2 = opPop()
            opPush(op1 + op2)
        else:
            print("[!] - Cannot add(). Incorrect parameter types")
    else:
        print("[!] - Cannot add(). Insufficient parameters")

def sub():
    if len(opstack) >= 2:
        if (type(opstack[-1]) is int or float) and (type(opstack[-2]) is int or float):
            op1 = opPop()
            op2 = opPop()
            opPush(op2 - op1)
        else:
            print("[!] - Cannot sub(). Incorrect parameter types")
    else:
        print("[!] - Cannot sub(). Insufficient parameters")

def mul():
    if len(opstack) >= 2:
        if (type(opstack[-1]) is int or float) and (type(opstack[-2]) is int or float):
            op1 = opPop()
            op2 = opPop()
            opPush(op1 * op2)
        else:
            print("[!] - Cannot mul(). Incorrect parameter types")
    else:
        print("[!] - Cannot mul(). Insufficient parameters")

def div():
    if len(opstack) >= 2:
        if (type(opstack[-1]) is int or float) and (type(opstack[-2]) is int or float):
            op1 = opPop()
            op2 = opPop()
            opPush(op2 / op1)
        else:
            print("[!] - Cannot div(). Incorrect parameter types")
    else:
        print("[!] - Cannot div(). Insufficient parameters")

def mod():
    if len(opstack) >= 2:
        if (type(opstack[-1]) is int or float) and (type(opstack[-2]) is int or float):
            op1 = opPop()
            op2 = opPop()
            opPush(op2 % op1)
        else:
            print("[!] - Cannot mod(). Incorrect parameter types")
    else:
        print("[!] - Cannot mod(). Insufficient parameters")

def eq():
    if len(opstack) >= 2:
        if (type(opstack[-1]) is int or float) and (type(opstack[-2]) is int or float):
            op1 = opPop()
            op2 = opPop()
            opPush(op1 == op2)
        else:
            print("[!] - Cannot eq(). Incorrect parameter types")
    else:
        print("[!] - Cannot eq(). Insufficient parameters")

def lt():
    if len(opstack) >= 2:
        if (type(opstack[-1]) is int or float) and (type(opstack[-2]) is int or float):
            op1 = opPop()
            op2 = opPop()
            opPush(op2 < op1)
        else:
            print("[!] - Cannot lt(). Incorrect parameter types")
    else:
        print("[!] - Cannot lt(). Insufficient parameters")

def gt():
    if len(opstack) >= 2:
        if (type(opstack[-1]) is int or float) and (type(opstack[-2]) is int or float):
            op1 = opPop()
            op2 = opPop()
            opPush(op2 > op1)
        else:
            print("[!] - Cannot gt(). Incorrect parameter types")
    else:
        print("[!] - Cannot gt(). Insufficient parameters")

#--------------------------string manipulators------------------------------------
def length():
    if (len(opstack) > 0):
        op = opPop()
        opPush(len(op) - 2)
    else:
        print("[!] - Cannot length(). Operator stack empty")

def get():
    if (len(opstack) > 1):
        if (type(opstack[-1]) is int) and (type(opstack[-2]) is str): #now works with strings feelsbad
            index = opPop()
            array = opPop()
            opPush(ord(array[index + 1]))
        else:
           print("[!] - Cannot get(). Incorrect parameter types")
    else:
        print("[!] - Cannot get(). Operator stack empty")

def getinterval():
    if (len(opstack) > 2):
        count = opPop()
        index = opPop()
        string = opPop()
        if ((type(string) is str) and (type(index) is int) and (type(count) is int) and index >= 0 and index < len(string) and count >= 0 and count <= len(string)):
            opPush('(' + string[index + 1:count + index + 1] + ')')
        else:
            print("[!] - Cannot getinterval(). Incorrect parameter types")
    else:
        print("[!] - Cannot getinterval(). Insufficient parameters in operator stack")

def put():
    char = opPop()
    index = opPop()
    array = opPop()

    strid = id(array)
    strlist = list(array)

    char = chr(char)
    strlist[index + 1] = char

    array = ''.join(strlist)
    size = len(opstack)

    for x in range(size):
        if(id(opstack[x]) == strid):
            opstack[x] = array
        
    for d in dictstack:
        for key in d.keys():
            if(id(d[key]) == strid):
                d[key] = array

#------------------------stack manipulators -------------------------------------
def dup():
    if (len(opstack) > 0):
        opPush(opstack[-1])
    else:
        print("[!] - Cannot dup(). Operator stack empty")

def copy():
    if (len(opstack) > 0):
        items = opPop()
        opstack.extend(opstack[-items:])
    else:
        print("[!] - Cannot copy(). Operator stack empty")

def pop():
    if (len(opstack) > 0):
        opPop()
    else:
        print("[!] - Cannot pop(). Operator stack empty")

def clear():
    del opstack[:]
    del dictstack[:]

def exch():
    if (len(opstack) > 1):
        op1 = opPop()
        op2 = opPop()
        opPush(op1)
        opPush(op2)
    else:
        print("[!] - Cannot exch(). Insufficient parameters in operator stack")

def roll():
    if (len(opstack) > 1):
        op1 = opPop()
        op2 = opPop()
        rollList = []
        for x in range(0, op2):
            rollList.append(opPop())

        if (op1 <= 0):
            rollList[:0] = rollList[op1:]
            rollList[op1:] = []            
        else:
            rollList[len(rollList):] = rollList[0:op1]
            rollList[0:op1] = []
            
        for x in reversed(rollList):
            opPush(x)
    else:
        print("[!] - Cannot roll(). Insufficient parameters in operator stack")

def stack():
    print("==============")

    for item in reversed(opstack):
        print(item)

    print("==============")

    for (index, item) in reversed(list(enumerate(dictstack))):
        top, d = item

        print("----", index, "----", top, "----")
        
        if (len(d) > 0):
            for key in d:
                print(key, d[key])

    print("==============")


#--------------------------dict manipulators -----------------------------------
def psDict():
    top = opPop()
    d = {}
    opPush(d)

def begin():
    if (len(opstack) > 0):       
        if (type(opstack[-1]) is dict):
            op = opPop()
            dictPush(op)
        else:
            print("[!] - Cannot begin(). Cannot push non-dictionary onto dictionary stack")
    else:
        print("[!] - Cannot begin(). Operator stack empty")

def end():
    if (len(dictstack) > 0):
        dictPop()
    else:
        print("[!] - Cannot end(). Dictionary stack empty")

def psDef(): 
    if (len(opstack) > 1):
        value = opPop()
        name = opPop()
        if (name.startswith('/')):
            define(name, value)           
        else:
            print("[!] - Cannot psDef(). Name does not start with /")
    else:
        print("[!] - Cannot psDef(). Operator stack empty")

#--------------------------- some operators: if, ifelse, for ---------------------------

def psAnd():
    if (len(opstack) > 1):
        if (type(opstack[-1]) is bool) and (type(opstack[-2]) is bool):
            op1 = opPop()
            op2 = opPop()
            opPush(op1 and op2)
        else:
            print("[!] - Cannot psAnd(). Either ", op1, " or ", op2, " is not a bool")
    else:
        print("[!] - Cannot psAnd(). Insufficient parameters")

def psOr():
    if (len(opstack) > 1):
        if (type(opstack[-1]) is bool) and (type(opstack[-2]) is bool):
            op1 = opPop()
            op2 = opPop()
            opPush(op1 or op2)
        else:
            print("[!] - Cannot psOr(). Either ", op1, " or ", op2, " is not a bool")
    else:
        print("[!] - Cannot psOr(). Insufficient parameters")

def psNot():
    if (len(opstack) > 0):
        if (type(opstack[-1]) is bool):
            op = opPop()
            opPush(not op)
        else:
            print("[!] - Cannot psNot(). ", op, " is not a bool")
    else:
        print("[!] - Cannot psNot(). Insufficient parameters")

def psIf():
    code = opPop()
    condition = opPop()
    if condition:
        interpretSPS(code, scope)
    else:
        print("[!] - Cannot If() - Condition is not a bool")

def psIfElse():
    elseCode = opPop()
    ifCode = opPop()
    condition = opPop()
    if isinstance(condition, bool):
        if condition:
            interpretSPS(ifCode, scope)
        else:
            interpretSPS(elseCode, scope)
    else:
        print("[!] - Cannot IfElse() - Condition is not a bool")

def psFor():
    code = opPop()
    end = opPop()
    index = opPop()
    start = opPop()

    if isinstance(code, list):
        if index > 0:
            for item in range(start, end + 1, index):
                opPush(item)
                interpretSPS(code, scope)
        else:
            for item in range(start, end - 1, index):
                opPush(item)
                interpretSPS(code, scope)
    else:
        print("[!] - Cannot psFor() - Input is not a list")

#--------------------------- parsing and stuff -----------------------------------

def tokenize(s):
    return re.findall("/?[a-zA-Z()][a-zA-Z0-9_()]*|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)

def groupMatching2(it):
    res = []
    for c in it:
        if c == '}':
            return res
        elif c=='{':
            res.append(groupMatching2(it))
        else:
            res.append(c)
    return False

def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if (isinstance(c, list)):
            res.append(parse(c))

        elif (c == '}'):
            return False

        elif (c == '{'):
            res.append(parse(groupMatching2(it)))

        elif (c == "true"):
            res.append(True)
        
        elif (c == "false"):
            res.append(False)

        elif (c.isdigit()):
            res.append(int(c))

        elif (c.startswith('-')):
            res.append(int(c))

        elif (c.startswith('[')):
            res.append([int(num) for num in c[1:-1].split(' ')])

        else:
            res.append(c)

    return res

def interpretSPS(code, scope):
    functions = {"add": add, "sub": sub, "mul": mul, "div": div, "mod": mod, "eq": eq, "lt": lt, "gt": gt,
                 "length": length, "get": get, "getinterval": getinterval, "put": put,
                 "dup": dup, "copy": copy, "pop": pop, "clear": clear, "exch": exch, "roll": roll, "stack": stack,
                 "dict": psDict, "begin": begin, "end": end, "def": psDef, 
                 "if": psIf, "ifelse": psIfElse, "for": psFor,
                 "and": psAnd, "or": psOr, "not": psNot}
    
    for token in code:
        try: 
            functions[token]() 
        except (KeyError, TypeError):
            try:
                i, val = lookup(token, scope)   
                if (isinstance(val, list)):                   
                    dictPush((i, {}))
                    interpretSPS(val, scope)
                    dictPop()
                else:
                    opPush(val)
            
            except:
                try:
                    opPush(token)
                except:
                    opPush(token)

def interpreter(s, scope):
    print()
    print("- - -", scope, "- - -")
    interpretSPS(parse(tokenize(s)), scope)
    print()

#--------------------------- testing ---------------------------

def test0():
    print(" - - - - - TEST0 - - - - -")
    input1 = """
        /x 4 def
        /g { x stack } def
        /f { /x 7 def g } def
        f
        """

    interpreter(input1, "static")
    clear()
    interpreter(input1, "dynamic")
    clear()


def test1():
    print(" - - - - - TEST1 - - - - -")
    input2 = """
        /m 50 def
        /n 100 def
        /egg1 {/m 25 def n} def
        /chic {
            /n 1 def
            /egg2 { n } def
            m n
            egg1
            egg2
            stack } def
        n
        chic
        """
    interpreter(input2, "static")
    clear()
    interpreter(input2, "dynamic")
    clear()

def test2():
    print(" - - - - - TEST2 - - - - -")
    input3 = """
        /x 10 def
        /A { x } def
        /C { /x 40 def A stack } def
        /B { /x 30 def /A { x } def C } def
        B
        """
    interpreter(input3, "static")
    clear()
    interpreter(input3, "dynamic")
    clear()

def test3():
    print(" - - - - - TEST3 - - - - -")
    input4 = """
        /out true def
        /xand { true eq {pop false} {true eq { false } { true } ifelse} ifelse 
        dup /x exch def stack} def 
        /myput { out dup /x exch def xand } def
        /f { /out false def  myput } def
        false f
        """
    interpreter(input4, "static")
    clear()
    interpreter(input4, "dynamic")
    clear()


def test4(): 
    print(" - - - - - TEST4 - - - - -")
    input5 =  """
        /x 10 def
        /A { x } def
        /B { /x 30 def /A { x stack } def /C { /x 40 def A } def C } def
        B
        """
    interpreter(input5, "static")
    clear()
    interpreter(input5, "dynamic")
    clear()

if __name__ == '__main__':
    test0()
    test1()
    test2()
    test3()
    test4()
    

