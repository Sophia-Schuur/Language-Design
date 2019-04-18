## Python Interpreter
An Interpreter for a simple Postscript-like language. The simplified language, SPS, has the following features of PS:
* Integer constants (123): In Python3 there exists no practical limit on the size of integers
* String constants (Hello): Strings delimited in parenthesis
* Name constants (/fact): Start with a / and letter followed by an arbitrary sequence of letters and numbers
* Names to be looked up in the dictionary stack (fact): For name constants, without the /
* Code constants: code between matched curly braces { ... }
* Built-in arithmetic operators
* Built-in string operators
* Built-in conditional operators
* Built-in loop operators
* Stack operators
* Dictionary creation operator
* Dictionary stack manipulators
* Name definition operator
* Defining and calling functions
* Print stack contents

#### Run:
Intended to run on Windows for Python3. Tests itself with built-in unit tests. 

Browse to directory and run `python "Python Interpreter.py"`.
