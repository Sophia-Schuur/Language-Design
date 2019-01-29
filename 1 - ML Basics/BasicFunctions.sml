(*Sophia Schuur
1/21/2019
This program performs several simple independent functions and respective tests. *)



(*Remove undesired chars from a string. Used to remove spaces in isPalindrome*)
fun removeChar(string, chars) =
  String.concat(String.tokens (fn c => String.isSubstring (str c) chars) string)


(*Capitalizes all chars of a string. Used to ignore casing in isPalindrome*)
fun Capitalize s =
  	let 
  		fun upper(char::rest) = Char.toUpper char::upper(rest)
        	| upper([]) = []
  	in 
  		implode(upper (explode s)) 
	end

(*Removes all of given value in list*)
fun removeAllInstances(value, []) = []
    | removeAllInstances(value, (head::rest)) =
     	if value = head
     		then removeAllInstances(value, rest)
    	else 
	 		head::removeAllInstances(value, rest);


(*- - - 1 - - -*)
(*Takes a tuple as an input where the first element of the tuple is a value
and the second is a list.
Returns true if the value exists in the list.
Returns false otherwise.
Function has type  ''a * ''a list -> bool *)
fun exists(value, []) = false
   | exists(value, head::list)  =	(*:: - Add element at beginning of list, return the new list*)
    if value = head		(*base case*)
    	then true
    else 
		exists(value, list);	

(* Explain in a comment why the type is ''a * ''a list -> bool and not  'a * 'a list -> bool  *)

(* This is because the equality type, denoted by ''a, is generated by the polymophic
equality operator (=), which determines if two values are equal. This means
that both of its operands must be of the same type, hence the use of equality types (''a). *)


(*Removes duplicates in a list*);
fun removeDuplicates ([]) = []
	| removeDuplicates(head::rest) = 
	    if exists(head, rest)
			then removeDuplicates(rest)			
		else 
			head::removeDuplicates(rest);

(*- - - 2 - - -*)
(*takes two lists as input and returns the union of those lists. 
Order does not matter but each value appears in output list only once.
Removes duplicate values found in one or both lists. 
Function has type ''a list -> ''a list -> ''a list.*)
fun listUnion(List1, List2) =
    let
       fun unionHelper(List1, []) = List1	(*Makes sure there are no duplicates from one OR both lists*)
          | unionHelper([], List2) = List2
          | unionHelper(List1, (L2::L2rest)) =
           if exists(L2, List1)
           		then L2::unionHelper(L2rest, removeAllInstances(L2, List1))
           		else L2::unionHelper(L2rest, List1)
       in
         unionHelper((removeDuplicates(List1)), (removeDuplicates(List2)))
	end;


(*- - - 3 - - -*)
(*Takes an index n, a value v and a list L and returns a new list L which is equal to the 
first L, except that its nth element is now v.
Function has type int -> 'a -> 'a list -> 'a list*)
fun replace (index, value, []) = []
    | replace (index, value, (head::rest)) =
        if index = 0			(*Base case for first index*)
            then (value::rest)	(*Append value to the rest of the list *)
	    else
	        head::(replace ((index-1), value, rest));	(*Decrement index*)


(*- - - 4 - - -*)
(*Takes a string (a class) and returns the list of courses which require that class as a prereq.
Function has type ('a * ''b list) list * ''b -> 'a list*)
 val prereqsList = [("Cpts122",["CptS121"]), ("CptS132",["CptS131"]), ("CptS223",["CptS122", "MATH216"]), ("CptS233",["CptS132", "MATH216"]), ("CptS260",["CptS223", "CptS233"]), 
                       ("CptS315",["CptS223", "CptS233"]), ("CptS317",["CptS122", "CptS132", "MATH216"]), ("CptS321",["CptS223", "CptS233"]), ("CptS322",["CptS223","CptS233"]), 
                       ("CptS350",["CptS223","CptS233", "CptS317"]), ("CptS355",["CptS223"]), ("CptS360",["CptS223","CptS260"]),("CptS370",["CptS233","CptS260"]),
                       ("CptS427",["CptS223","CptS360", "CptS370", "MATH216", "EE234"])];

fun prereqFor([], class) = []
	| prereqFor((list, first::last)::rest, class) =
		if exists(class, first::last) = true
			then list::prereqFor(rest, class)
		else
			prereqFor(rest, class);

(*Explain in a comment why the type 
is ('a * ''b list) list * ''b -> 'a list but not (''a * ''a list) list * ''a-> ''a list *)

(*'a denotes any possible type. The separation of 'b and 'a indicates that a and b are different types.
The '' means that the items in the ''b's must all be the same type. *)


(*- - - 5 - - -*)
(*Returns true if a string is a palindrome, false otherwise.
Case insensitive and ignores spaces!*)
fun isPalindrome (string) =
	let	
		val caps = Capitalize(string)				(*Capitalizes string (i.e ignore case)*)
		val newstring = removeChar(caps, " ");		(*Remove spaces*)
		val chars = explode(newstring)				(*Return list of chars in string*)
	in 
	  	chars = rev(chars)	(*reverse chars*)
  end;


(*- - - 6 - - -*)
(*Takes an int and a list and returns a list of lists containing the max num of consecutive
elements from initial list that sup up to N or less.
Leftover elements are included as the last sub list with a sum less than N.
If an element in the input list is greater than N, it gets its own sub list.
Function type is int -> int list -> int list list *)
fun groupSumtoN(N, []) = []
	| groupSumtoN(N, L1) = 

	let 
		fun sublist(N, head::rest, []) = sublist(N, rest, head::[])
		| sublist(N, [], L1) = L1::[]
		| sublist(N, head::rest, L2) = 

		let
			fun combine([]) = 0
			| combine(x::rest) = x + (combine(rest));
			in
				if((combine(L2) + head <= N))			(*Is the  element smaller than N?*)
					then sublist(N, rest, head::L2)		(*Keep adding to same sublist*)
				else						
					L2::sublist(N, rest, head::[])	(*Otherwise it gets its own list*)
			end;
		in	
			sublist(N, L1, [])
		end;

(*- - - TESTS - - -*)
(* Tests for exists() *)
(* Will print a boolean T/F whether or not each given assertion is true or false.*)
fun existsTests() =
    let
      val existsT1 = (exists(8,[7]) = false )
      val existsT2 = (exists("one",["two","one"]) = true )
      val existsT3 = (exists(true,[false,false]) = false )

	  val existsT4 = exists([1,3],[[7,3],[1,3],[1,6],[2,2]]) = true
	  val existsT5 = exists("A",["AAA", "AA", "A"]) = true
    in
	print("\n- - - - - - - - - - - - - -\n" ^ 
      "\n[!] - Starting Exists Tests\n" ^
	  " Staring Given Tests:\n" ^
            "  Test1: " ^ Bool.toString(existsT1) ^ "\n" ^
            "  Test2: " ^ Bool.toString(existsT2) ^ "\n" ^
            "  Test3: " ^ Bool.toString(existsT3) ^ "\n" ^
			" Ending Given Tests\n" ^
			" Starting My tests:\n" ^
            "  Test4: " ^ Bool.toString(existsT4) ^ "\n" ^
            "  Test5: " ^ Bool.toString(existsT5) ^ "\n" ^
			" Ending My Tests\n" ^
			"[!] - Ending Exists Tests\n\n")
			
    end;
	val _ = existsTests()

(*Tests for listUnion() *)
(*Will print a boolean T/F whether or not each given assertion is true or false.*)
fun  listUnionTests() =
	let	
		val unionT1 =listUnion([1,3,4], [2,3,4,5]) = [2,1,3,4,5]
		val unionT2 =listUnion([1,1,2,3,3,3], [1,3,4,5]) =  [1,2,3,4,5]
		val unionT3 =listUnion(["a","b","c"], ["b","b","d"]) = ["b","a","d","c"]
		val unionT4 =listUnion([[1,2],[2,3]], [[1],[2,3],[2,3]]) = [[1],[1,2],[2,3]]

		val unionT5 =listUnion([1,2,2,2,3,3,4], [2,2,2,3,4,5,1]) = [2,1,3,4,5]
		val unionT6 =listUnion([0,99], [99,0,1]) = [99,0,1]
		
	in
	print("\n- - - - - - - - - - - - - -\n" ^ 
	"\n[!] - Starting Union Tests\n" ^
	  " Staring Given Tests:\n" ^
            "  Test1: " ^ Bool.toString(unionT1) ^ "\n" ^
            "  Test2: " ^ Bool.toString(unionT2) ^ "\n" ^
            "  Test3: " ^ Bool.toString(unionT3) ^ "\n" ^
            "  Test4: " ^ Bool.toString(unionT4) ^ "\n" ^
            " Ending Given Tests\n" ^
			" Starting My tests:\n" ^
			"  Test5: " ^ Bool.toString(unionT5) ^ "\n" ^
			"  Test6: " ^ Bool.toString(unionT6) ^ "\n" ^
			" Ending My Tests\n" ^
			"[!] - Ending Union Tests\n\n")
	end;
	val _ = listUnionTests()

fun replaceTests() =
	let
      val replaceT1 = replace (3, 40, [1, 2, 3, 4, 5, 6]) = [1,2,3,40,5,6] 
      val replaceT2 = replace (0, "X", ["a", "b", "c", "d"]) = ["X","b","c","d"] 
      val replaceT3 = replace(6, 7, [1,2,3,4,5]) = [1,2,3,4,5] 

	  val replaceT4 =  replace(1, "hello", ["hello", "how", "are", "you"]) = ["hello", "hello", "are", "you"]
	  val replaceT5 =  replace(2, 100, [100,2,3]) = [100,2,100]
    in
	print("\n- - - - - - - - - - - - - -\n" ^ 
      "\n[!] - Starting Replace Tests\n" ^
	  " Staring Given Tests:\n" ^
            "  Test1: " ^ Bool.toString(replaceT1) ^ "\n" ^
            "  Test2: " ^ Bool.toString(replaceT2) ^ "\n" ^
            "  Test3: " ^ Bool.toString(replaceT3) ^ "\n" ^
			" Ending Given Tests\n" ^
			" Starting My tests:\n" ^
            "  Test4: " ^ Bool.toString(replaceT4) ^ "\n" ^
            "  Test5: " ^ Bool.toString(replaceT5) ^ "\n" ^
			" Ending My Tests\n" ^
			"[!] - Ending Replace Tests\n\n")
			
    end;
	val _ = replaceTests()

(*Tests for preregFor() *)
(*Will print a boolean T/F whether or not each given assertion is true or false.*)
fun prereqForTest () =
   let 
     val prereqForT1 = (prereqFor (prereqsList,"CptS260") = ["CptS360","CptS370"] )
     val prereqForT2 = (prereqFor (prereqsList,"CptS223") = ["CptS260","CptS315","CptS321","CptS322","CptS350","CptS355","CptS360","CptS427"] )
     val prereqForT3 = (prereqFor (prereqsList,"CptS355") = [] )

	  val prereqForT4 = (prereqFor (prereqsList,"CptS317") = ["CptS350"] )
	  val prereqForT5 = (prereqFor (prereqsList,"MATH216") = ["CptS223","CptS233","CptS317","CptS427"] )
   in 
   print("\n- - - - - - - - - - - - - -\n" ^ 
      "\n[!] - Starting PrereqFor Tests\n" ^
	  " Staring Given Tests:\n" ^
            "  Test1: " ^ Bool.toString(prereqForT1) ^ "\n" ^
            "  Test2: " ^ Bool.toString(prereqForT2) ^ "\n" ^
            "  Test3: " ^ Bool.toString(prereqForT3) ^ "\n" ^
			" Ending Given Tests\n" ^
			" Starting My tests:\n" ^
            "  Test4: " ^ Bool.toString(prereqForT4) ^ "\n" ^
            "  Test5: " ^ Bool.toString(prereqForT5) ^ "\n" ^
			" Ending My Tests\n" ^
			"[!] - Ending PrereqFor Tests\n\n")		
   end
val _ = prereqForTest()


(*Tests for isPalindrome() *)
(*Will print a boolean T/F whether or not each given assertion is true or false.*)
fun isPalindromeTests() =
	let
      val palT1 = isPalindrome("a01 02 2010A") = true
	  val palT2 = isPalindrome("Doc note I dissent a fast never prevents a fatness I diet on cod") = true
      val palT3 = isPalindrome("Yreka Bakery") = true
      val palT4 = isPalindrome("top cart pop tracPOT") = true

	  val palT5 =  isPalindrome("1rAce CaR1") = true
	  val palT6 =  isPalindrome("2rAce CaR1") = false
    in
	print("\n- - - - - - - - - - - - - -\n" ^ 
      "\n[!] - Starting Palindrome Tests\n" ^
	  " Staring Given Tests:\n" ^
            "  Test1: " ^ Bool.toString(palT1) ^ "\n" ^
            "  Test2: " ^ Bool.toString(palT2) ^ "\n" ^
            "  Test3: " ^ Bool.toString(palT3) ^ "\n" ^
            "  Test4: " ^ Bool.toString(palT4) ^ "\n" ^
            " Ending Given Tests\n" ^
			" Starting My tests:\n" ^
			"  Test6: " ^ Bool.toString(palT5) ^ "\n" ^
			"  Test7: " ^ Bool.toString(palT6) ^ "\n" ^
			" Ending My Tests\n" ^
			"[!] - Ending Palindrome Tests\n\n")
			
    end;
	val _ = isPalindromeTests()

(*Tests for groupSumtoN() *)
(*Will print a boolean T/F whether or not each given assertion is true or false.*)
fun groupSumtoNTests() =
	let
      val sumT1 = groupSumtoN(15, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) = [[5,4,3,2,1],[7,6],[8],[9],[10]]
	  val sumT2 = groupSumtoN(11, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) = [[4,3,2,1],[6,5],[7],[8],[9],[10]]
      val sumT3 = groupSumtoN(1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] ) = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
      val sumT4 = groupSumtoN(5, []) = []

	  val sumT5 =  groupSumtoN(5, [1, 2, 3, 4, 5]) =  [[2,1],[3],[4],[5]]
	  val sumT6 =  groupSumtoN(500, [1, 2, 3, 4, 5, 50]) =  [[50,5,4,3,2,1]]
    in
	print("\n- - - - - - - - - - - - - -\n" ^ 
      "\n[!] - Starting groupSumToN Tests\n" ^
	  " Staring Given Tests:\n" ^
            "  Test1: " ^ Bool.toString(sumT1) ^ "\n" ^
            "  Test2: " ^ Bool.toString(sumT2) ^ "\n" ^
            "  Test3: " ^ Bool.toString(sumT3) ^ "\n" ^
            "  Test4: " ^ Bool.toString(sumT4) ^ "\n" ^
            " Ending Given Tests\n" ^
			" Starting My tests:\n" ^
			"  Test6: " ^ Bool.toString(sumT5) ^ "\n" ^
			"  Test7: " ^ Bool.toString(sumT6) ^ "\n" ^
			" Ending My Tests\n" ^
			"[!] - Ending groupSumToN Tests\n\n")
			
    end;
	val _ = groupSumtoNTests()