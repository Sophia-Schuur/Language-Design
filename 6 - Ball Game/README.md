## BallGame
A simple ball game written in Java. Click on as many balls as you can and earn points for each click. 
The game ends when all the balls fly out the screen.

Needs jdk version 12 (or later?) to run from command line. Make sure Windows can find the Java compiler by adding
the Java installation directory to the Windows 'Path' environment variable. 

Uses command line arguments to set size and number of balls. 

#### Run:
Browse to directory and compile with `javac *.java`. Run with `java BallGame <num balls> <balltype> <ballsize>`.

For example: `java BallGame 4 basic 0.10 bounce 0.05 shrink 0.13 split 0.05`

#### Known bugs: 
* Stalls upon clicking a split ball too quickly. 
* Sometimes incorrectly counts one click as multiple.

