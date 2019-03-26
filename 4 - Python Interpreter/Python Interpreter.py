# Sophia Schuur 11519303
# 3/21/2019
# Skeleton for a Python interpreter. 

# Windows intended.

#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  #assuming top of the stack is the end of the list

# Now define the helper functions to push and pop values on the opstack (i.e, add/remove elements to/from the end of the Python list)
# Remember that there is a Postscript operator called "pop" so we choose different names for these functions.
# Recall that `pass` in python is a no-op: replace it with your code.

def opPop():
    if (len(opstack) > 0):
        return opstack.pop()
    else:
        print("[!] - Operator stack empty")
    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.

def opPush(value):
    opstack.append(value)

#-------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to define name, and to lookup a name

def dictPop():
    if (len(dictstack) > 0):
        return dictstack.pop()
    else:
        print("[!] - Dictionary stack empty")

    # dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    if (type (d) is dict):
        dictstack.append(d)
    else:
        print("[!] - Dictionary stack empty")
    #dictPush pushes the dictionary ‘d’ to the dictstack. Note that, your interpreter will call dictPush only when Postscript “begin” operator is called. “begin” should pop the empty dictionary from the opstack and push it onto the dictstack by calling dictPush.

def define(name, value):
    if(len(dictstack) == 0):
        d = {}
        d[name] = value
        dictPush(d)
    else:
        (dictstack[-1])[name] = value

    #add name:value pair to the top dictionary in the dictionary stack. Keep the '/' in the name constant. 
    # Your psDef function should pop the name and value from operand stack and call the “define” function.

def lookup(name):
    newName = '/' + name
    for d in reversed(dictstack):
        if newName in d:
            return d[newName]
    else:
        print("[!] - Name not found in dictionary")

    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.

#--------------------------- 10% -------------------------------------
# Arithmetic and comparison operators: add, sub, mul, div, mod, eq, lt, gt
#Make sure to check the operand stack has the correct number of parameters and types of the parameters are correct.

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

#--------------------------- 15% -------------------------------------
# String operators: define the string operators length, get, getinterval, put
def length():
    if (len(opstack) > 0):
        op = opPop()
        if (type(op) is list):
            opPush(len(op))
        else:
            print("[!] - Cannot length(). Parameter not a string")
    else:
        print("[!] - Cannot length(). Operator stack empty")


def get():
    if (len(opstack) > 1):
        if (type(opstack[-1]) is int) and (type(opstack[-2]) is list): # instead of str, list is more versatile. works on any list types instead of just strings!
            index = opPop()
            array = opPop()
            opPush(array[index])
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
    if (len(opstack) > 2):
        string = opPop() 
        index = opPop()
        asc = opPop()
        opPush(string[:index] + chr(asc) + string[index+1:])
    else:
        print("[!] - Cannot put(). Insufficient parameters in operator stack")

#--------------------------- 25% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, pop, clear, exch, roll, stack
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
    if (len(opstack) == 0):
        print("[]")
    else:
        print("[ ", end ="")
        for item in reversed(opstack):
            print(item, "",  end ="")
        print("]")

#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

def psDict():
    d = dict()
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
        if (type(opstack[-1]) is int) and (type(opstack[-2]) is str) and (opstack[-2].startswith('/') is True):
            value = opPop()
            name = opPop()
            define(name, value)
        else:
            print("[!] - Incorrect parameter types")
    else:
        print("[!] - Cannot psDef(). Operator stack empty")
# --------------------------------------------------------------------
## Sample tests #
# --------------------------------------------------------------------
def testDefine():
    clear()
    define("/n1", 8)
    if lookup("n1") != 8:
        return False
    return True

def testLookup():
    clear()
    opPush("/n1")
    opPush(3)
    psDef()
    if lookup("n1") != 3:
        return False
    return True

def testAdd():
    clear()
    opPush(1)
    opPush(2)
    add()
    if opPop() != 3:
        return False
    return True

def testSub():
    clear()
    opPush(15.6)
    opPush(8.2)
    sub()
    if opPop() != 7.4:
        return False
    return True

def testMul():
    clear()
    opPush(5)
    opPush(6.5)
    mul()
    if opPop() != 32.5:
        return False
    return True

def testDiv():
    clear()
    opPush(8)
    opPush(2)
    div()
    if opPop() != 4:
        return False
    return True

def testMod():
    clear()
    opPush(16)
    opPush(9)
    mod()
    if opPop() != 7:
        return False
    return True

def testEq():
    clear()
    opPush(1)
    opPush(1)
    eq()
    if opPop() != True:
        return False
    return True

def testLt():
    clear()
    opPush(1)
    opPush(2)
    lt()
    if opPop() != True:
        return False
    return True

def testGt():
    clear()
    opPush(2)
    opPush(1)
    gt()
    if opPop() != True:
        return False
    return True

def testLength():
    clear()
    opPush([1,2,3])
    length()
    if opPop() != 3:
        return False
    return True


def testGet():
    clear()
    opPush([3,6,9])
    opPush(1)
    get()
    if opPop() != 6:
        return False
    return True


def testGetinterval():
    clear()
    opPush("(HelloWorld)")
    opPush(0)
    opPush(5)
    getinterval()
    if opPop() != "(Hello)":
        return False
    return True

def testPut():
    clear()
    opPush(72)
    opPush(0)
    opPush('helloworld')
    put()
    if(opPop() != 'Helloworld'):
        return False
    return True

def testDup():
    clear()
    opPush(13)
    dup()
    if opPop()!=opPop():
        return False
    return True

def testExch():
    opPush(10)
    opPush("/x")
    exch()
    if opPop()!=10 and opPop()!="/x":
        return False
    return True

def testPop():
    l1 = len(opstack)
    opPush(10)
    pop()
    l2= len(opstack)
    if l1!=l2:
        return False
    return True

def testRoll():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(4)
    opPush(-2)
    roll()
    if opPop()!=3 and opPop()!=2 and opPop()!=5 and opPop()!=4 and opPop()!=1:
        return False
    return True

def testCopy():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(2)
    copy()
    if opPop()!=5 and opPop()!=4 and opPop()!=5 and opPop()!=4 and opPop()!=3 and opPop()!=2:
        return False
    return True

def testClear():
    opPush(10)
    opPush("/x")
    clear()
    if len(opstack)!=0:
        return False
    return True

def testDict():
    opPush(1)
    psDict()
    if opPop()!={}:
        return False
    return True

def testBegin():
    clear()
    opPush({})
    begin()
    if dictPop() != {}:
        return False
    return True

def testEnd():
    clear()
    dictPush({})
    end()
    if len(dictstack) != 0:
        return False
    return True

def testBeginEnd():
    opPush("/x")
    opPush(3)
    psDef()
    opPush({})
    begin()
    opPush("/x")
    opPush(4)
    psDef()
    end()
    if lookup("x")!=3:
        return False
    return True

def testpsDef():
    clear()
    opPush("/sailed")
    opPush(5)
    psDef()
    if lookup("sailed")!=5:
        return False
    return True

def testpsDef2():
    clear()
    opPush("/ocean")
    opPush(15)
    psDef()
    opPush(5)
    psDict()
    begin()
    if lookup("ocean")!=15:
        end()
        return False
    end()
    return True

def main_part1():
    testCases = [('define',testDefine),('lookup',testLookup),('add', testAdd), ('sub', testSub),('mul', testMul),
                 ('div', testDiv),  ('mod', testMod), ('lt', testLt), ('gt', testGt), ('eq', testEq),
                 ('length', testLength),('get', testGet), ('getinterval', testGetinterval),
                 ('put', testPut), ('dup', testDup), ('exch', testExch), ('pop', testPop), ('roll', testRoll),
                 ('copy', testCopy), ('clear', testClear), ('dict', testDict), ('beginend', testBeginEnd), ('begin', testBegin),('end', testEnd),
                 ('psDef', testpsDef), ('psDef2', testpsDef2)]
    # add you test functions to this list along with suitable names
    failedTests = [testName for (testName, testProc) in testCases if not testProc()]
    if failedTests:
        return ('Some tests failed', failedTests)
    else:
        return ('All part-1 tests OK')

if __name__ == '__main__':
    print(main_part1())