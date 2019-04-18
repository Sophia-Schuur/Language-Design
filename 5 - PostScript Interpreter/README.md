## PostScript Interpreter
An interpreter for a scoped simple Postscript-like language - SSPS. SSPS has no `dict`, `begin` or `end` operations. 
Instead, each time a postscript function is called a new Dictionary is automatically pushed on the Dictionary stack.

#### Run: 
Intended to run on Windows for Python3. 

Browse to directory and run `python "SSPS Interpreter.py"`.

#### Known Bugs: 
* Dynamic scoping *seemingly* off. Does not always return expected dictstack top.


