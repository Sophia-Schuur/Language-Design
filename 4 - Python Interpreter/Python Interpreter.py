# Sophia Schuur
# 4/13/2019
# An Interpreter for a Simple Postscript-like Language

# Windows intended.

import re

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
    if (type (d) is dict):
        dictstack.append(d)
    else:
        print("[!] - Dictionary stack empty")

def define(name, value):
    if(len(dictstack) == 0):
        d = {}
        d[name] = value
        dictPush(d)
    else:
        (dictstack[-1])[name] = value

def lookup(name):
    for d in reversed(dictstack):
        if d.get('/'+name):
            return d.get('/'+name)         
    return None

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
    # if (len(opstack) == 0):
    #     print("[]")
    # else:
    #     print("[ ", end ="")
    #     for item in reversed(opstack):
    #         print(item, "",  end ="")
    #     print("]")
    for item in reversed(opstack):
        print(item)

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

#---------------------------PART 2 parsing and stuff -----------------------------------
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

def interpretSPS(code):
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
                val = lookup(token)   
                if isinstance(val, list):
                    interpretSPS(val)
                else:
                    opPush(int(val))
            except:
                try:
                    opPush(int(token))
                except:
                    opPush(token)

def interpreter(s):               
    interpretSPS(parse(tokenize(s)))


#--------------------------- some operators, if, ifelse, for ---------------------------
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
        interpretSPS(code)
    else:
        print("[!] - Cannot If() - Condition is not a bool")

def psIfElse():
    elseCode = opPop()
    ifCode = opPop()
    condition = opPop()
    if isinstance(condition, bool):
        if condition:
            interpretSPS(ifCode)
        else:
            interpretSPS(elseCode)
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
                interpretSPS(code)
        else:
            for item in range(start, end - 1, index):
                opPush(item)
                interpretSPS(code)
    else:
        print("[!] - Cannot psFor() - Input is not a list")


#--------------------------- testing ---------------------------
def testPut(): 
    print(" - - - - - TESTPut - - - - -")  
    opPush("(This is a test _)")
    dup()
    opPush("/s")
    exch()
    psDef()
    dup()
    opPush(15)
    opPush(48)
    put()
    stack()
    if lookup("s") != "(This is a test 0)" or opPop()!= "(This is a test 0)":
        return False
    return True

def test1():
    print(" - - - - - TEST1 - - - - -")
    input1 = """ /square { dup mul } def (square) 4 square dup 16 eq {(pass)} {(fail)} ifelse stack """
    clear()
    interpreter(input1)
    if (opPop() != "(pass)" and opPop != 16 and opPop() != "(square)"):
        return False
    else:
        return True

def test2():
    print(" - - - - - TEST2 - - - - -")
    input2 = """ (facto) dup length /n exch def /fact { 0 dict begin /n exch def n 2 lt { 1} {n 1 sub fact n mul } ifelse end } def n fact stack """
    clear()
    interpreter(input2)
    if (opPop() != 120 and opPop() != "(facto)"):
        return False
    else:
        return True

def test3():
    print(" - - - - - TEST3 - - - - -")
    input3 = """ /fact{ 0 dict begin /n exch def 1 n -1 1 {mul} for end } def 6 fact stack """ 
    clear()
    interpreter(input3)
    if (opPop() != 720):
        return False
    else:
        return True

def test4():
    print(" - - - - - TEST4 - - - - -")
    input4 = """ /lt6 { 6 lt } def  1 2 3 4 5 6 4 -3 roll dup dup lt6 {mul mul mul} if stack""" 
    clear()
    interpreter(input4)
    if (opPop() != 300 and opPop() != 6 and opPop() != 2 and opPop() != 1):
        return False
    else:
        return True

def test5():
    print(" - - - - - TEST5 - - - - -")
    input5 = """ (CptS355_HW5) 4 3 getinterval (355) eq {(You_are_in_CptS355)} if stack """
    clear()
    interpreter(input5)
    if (opPop() != "(You_are_in_CptS355)"):
        return False
    else:
        return True

def test6():
    print(" - - - - - TEST6 - - - - -")
    input6 = """ /pow2 {/n exch def (pow2_of_n_is) dup 8 n 48 add put 1 n -1 1 {pop 2 mul} for } def (Calculating_pow2_of_9) dup 20 get 48 sub pow2 stack """
    clear()
    interpreter(input6)
    if (opPop() != 512 and opPop() != "(Pow2_of_9_is)" and opPop() != "(Calculating_pow2_of_9)"):
        return False
    else:
        return True

def main_part2():
    testCases = [('put',testPut), ('test1', test1), ('test2', test2), ('test3', test3), ('test4', test4), ('test5', test5), ('test6', test6)]

    failedTests = [testName for (testName, testProc) in testCases if not testProc()]
    if failedTests:
        return ('Some tests failed', failedTests)
    else:
        return ('All part-2 tests OK')

if __name__ == '__main__':
    print(main_part2())

