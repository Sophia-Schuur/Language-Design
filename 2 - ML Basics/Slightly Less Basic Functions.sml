(*Sophia Schuur
2/2/2019
This program performs several simple independent functions and respective tests. *)

Control.Print.printDepth := 100;

fun revAppend ([],L) = L 
| revAppend(x::rest,L) = revAppend(rest,x::L); 

fun reverse L = revAppend(L,[]); 

fun fold f base [] = base  
| fold f base (x::rest) = f x (fold f base rest);

fun filter pred [] = [] | filter pred(x::rest) = if(pred x) then x::(filter pred rest) 
	else(filter pred rest)


(*- - - 1a - - -*)
(*
 * Takes two lists of integers, L1 and L2, each already in ascending order. 
 * Returns a merged list that is also in ascending order. 
 * The resulting list should include the elements from both lists and may include duplicates.
 *
 * Type: int list -> int list -> int list 
 *)
fun merge2 L1 [] = L1
	| merge2 [] L2 = L2
	| merge2 (L1::r1) (L2::r2) = 
    if L1 < L2 
        then L1::merge2 r1 (L2::r2)
    else 
        L2::merge2 (L1::r1) r2;

(*- - - 1b - - -*) (*NEEDS WORK*)
(*
 * merge2 as tail-recursive
 *
 * Type: int list -> int list -> int list 
 *)

 
fun merge2Tail L1 L2 =

let 
    fun helper(L1, [], acc) = ( L1@acc)
        | helper ([],L2, acc) = ( rev acc@L2)
        | helper (L1::r1, L2::r2, acc) = 
        if L1 < L2 
            then helper (r1, L2::r2, (L1::acc))
        else
            helper (L1::r1, r2, (L2::acc))
	in
	(helper(L1, L2, []))
end;


(*- - - 1c - - -*)
(*
 * Use merge2 and fold.
 * Takes a list of lists already in ascending order.
 * Returns new list containing all of the elements in sublists in ascending order.
 *
 * Type: int list list -> int list 
 *)

fun mergeN L1 = fold merge2 [] L1;


(*- - - 2a - - -*)
(*
 * Takes two ints v1 and v2 and a list L.
 * Returns the values in L which are greater than v1 and less than v2 (exclusive).
 * 
 * Type: int -> int -> int list -> int list
 *)
fun getInRange v1 v2 L = 
    let
      val pred = fn v1 => fn v2 => fn x => 
        if x < v2 andalso x > v1
          then true
        else 
          false;
    in
      filter (pred v1 v2) L  
    end;


(*- - - 2b - - -*)
(*
 * Uses getInRange.
 * Takes two ints v1 and v2 and a nested list L.
 * Returns total number of values in L greater than v1 and less than v2 (exclusive)
 * Must use higher order function (fold/map/filter).
 *
 * Type: int -> int -> int list list -> int
*)

fun countInRange v1 v2 L = 
  let 
    fun one x = 1;
    fun add x y = x+y;
  in
    fold add 0 (map (fold add 0) (map (map one) (map (getInRange v1 v2) L)))
  end;


(*- - - 3a - - -*)
(*
 * Takes two lengthUnit values and calculates the sum of those in inches.
 *
 * Type: lengthUnit -> lengthUnit -> lengthUnit
 *)

datatype lengthUnit = INCH of int | FOOT of int | YARD of int

	fun addLengths (INCH v1) (INCH v2) = INCH(v1 + v2)
	| addLengths (FOOT v1) (FOOT v2) = INCH(12*v1 + 12*v2)
	| addLengths (YARD v1) (YARD v2) = INCH(36*v1 + 36*v2)

	| addLengths (INCH v1) (FOOT v2) = INCH(v1 + 12*v2)
	| addLengths (FOOT v1) (INCH v2) = INCH(12*v1 + v2)

	| addLengths (INCH v1) (YARD v2) = INCH(v1 + 36*v2)
	| addLengths (YARD v1) (INCH v2) = INCH(36*v1 + v2)

	| addLengths (FOOT v1) (YARD v2) = INCH(12*v1 + 36*v2)
	| addLengths (YARD v1) (FOOT v2) = INCH(36*v1 + 12*v2)

(*- - - 3b - - -*)
(*
 * Takes nested list of lengthUnit.
 * Calculates sum of that in INCHs.
 *
 * Type: lengthUnit list list -> lengthUnit
 *)
fun addAllLengths L = 
  let
    fun add x y = addLengths x y;
  in
    fold add (INCH 0) (map (fold add (INCH 0)) L)
  end;

(*- - - 4a - - -*)
(*
 * Takes an int tree. 
 * Returns the sum of the values stored in the LEAVES only.
 * 
 * Type: int tree -> int
 *)

datatype 'a tree = LEAF of 'a | NODE of 'a * ('a tree) * ('a tree)

fun sumTree (LEAF n) = n
  | sumTree (NODE (n, left, right)) = (sumTree left) + (sumTree right)


(*- - - 4b - - -*)
(*
 * Takes an int tree.
 * Returns an int tree where the interior nodes store the sum of the leaf values below them.
 *
 * Type: int tree -> int tree
 *)

fun createSumTree (LEAF n) = LEAF(n)
  | createSumTree (NODE (n, left, right)) = NODE((sumTree(left) + sumTree(right)), createSumTree(left), createSumTree(right))


(* - - - 4/5c - - - *)
(*
 * Tests variables for tree functions.
*)
datatype 'a listTree = listLEAF of ('a list) | listNODE of ('a listTree list)

val t1 = NODE (1, NODE (2, NODE (3,LEAF 4, LEAF 5), LEAF 6), NODE(7, LEAF 8, LEAF 9));
(* Type: 'sumTree t1;' into prompt. *)
	(* returns 32 *)
val t2 = NODE (0, NODE(0, LEAF 4, NODE (0,LEAF 8, LEAF 9)), NODE(0, NODE(0,LEAF 10, NODE (0, LEAF 12, LEAF 13)), LEAF 7))
(* Type: 'sumTree t2;' into prompt. *)
	(* returns 63 *)
val t3 = NODE (0,NODE(0, NODE (0,LEAF 4, LEAF 5), LEAF 6), NODE(0, LEAF 8, LEAF 9));
(* Type: 'createSumTree t3;' into prompt. *)
	(* returns NODE (32, NODE (15,NODE (9,LEAF 4,LEAF 5),LEAF 6),NODE (17,LEAF 8,LEAF 9)) *)
val t4 = listNODE( [ listNODE ([ listLEAF [1,2,3],listLEAF [4,5], listNODE([listLEAF [6], listLEAF []]) ]), listNODE([]), listLEAF [7,8], listNODE([listLEAF [], listLEAF []]) ]);
(* Type: 'foldListTree add 0 t4;' into prompt. *)
    (* returns 36 *)


(*- - - 5 - - -*)
(*
 * Takes a function f, base value base and a listTree t.
 * Combines values in the lists of the leaf notes in tree t by applying function f.
 *
 * Type: ('a -> 'a -> 'a) -> 'a -> 'a listTree -> 'a
 *)

fun foldListTree f base (listLEAF n) = fold f base n
  | foldListTree f base (listNODE n) = fold f base (map (foldListTree f base) n)



(*
 * * * * * * * * * * * TESTS * * * * * * * * * * *
*)

(*
 * merge2 Tests
 *)
fun merge2Tests() =
	let
      val merge2T1 = merge2 [2,5,6,8,9] [1,3,4,5,7,8,10] = [1,2,3,4,5,5,6,7,8,8,9,10]
	  val merge2T2 = merge2 [1,2] [0,10,12] = [0,1,2,10,12]
      val merge2T3 = merge2 [1,3,3,5,5] [~1,2,4] = [~1,1,2,3,3,4,5,5]
      val merge2T4 = merge2 [1,2,3] [] = [1,2,3]

    in
	print("\n- - - - - - - - - - - - - -\n" ^ 
      "\n[!] - Starting merge2() Tests\n" ^
            "  Test1: " ^ Bool.toString(merge2T1) ^ "\n" ^
            "  Test2: " ^ Bool.toString(merge2T2) ^ "\n" ^
            "  Test3: " ^ Bool.toString(merge2T3) ^ "\n" ^
            "  Test4: " ^ Bool.toString(merge2T4) ^ "\n" ^
			"[!] - Ending merge2() Tests\n\n")		
    end;
	val _ = merge2Tests()


(*
 * merge2Tail Tests
 *)
fun merge2TailTests() =
	let
      val mergeTailT1 = merge2Tail [2,5,6,8,9] [1,3,4,5,7,8,10] = [1,2,3,4,5,5,6,7,8,8,9,10]
	  val mergeTailT2 = merge2Tail [1,2] [0,10,12] = [0,1,2,10,12]
      val mergeTailT3 = merge2Tail [1,3,3,5,5] [~1,2,4] = [~1,1,2,3,3,4,5,5]
      val mergeTailT4 = merge2Tail [1,2,3] [] = [1,2,3]

    in
	print("\n- - - - - - - - - - - - - -\n" ^ 
      "\n[!] - Starting merge2Tail() Tests\n" ^
            "  Test1: " ^ Bool.toString(mergeTailT1) ^ "\n" ^
            "  Test2: " ^ Bool.toString(mergeTailT2) ^ "\n" ^
            "  Test3: " ^ Bool.toString(mergeTailT3) ^ "\n" ^
            "  Test4: " ^ Bool.toString(mergeTailT4) ^ "\n" ^
			"[!] - Ending merge2Tail() Tests\n\n")		
    end;
	val _ = merge2TailTests()


(*
 * mergeN Tests
 *)
fun mergeNTests() =
	let
      val mergeNT1 = mergeN [[1,2],[10,12],[2,5,6,8,9]] = [1,2,2,5,6,8,9,10,12]
	  val mergeNT2 = mergeN [[3,4],[~3,~2,~1],[1,2,5,8,9]] = [~3,~2,~1,1,2,3,4,5,8,9]
    
    in
	print("\n- - - - - - - - - - - - - -\n" ^ 
      "\n[!] - Starting mergeN() Tests\n" ^
            "  Test1: " ^ Bool.toString(mergeNT1) ^ "\n" ^
            "  Test2: " ^ Bool.toString(mergeNT2) ^ "\n" ^
			"[!] - Ending mergeN() Tests\n\n")		
    end;
	val _ = mergeNTests()

(*
 * getInRange Tests
 *)
fun getInRangeTests() =
	let
      val getInRangeT1 = getInRange 3 10 [1,2,3,4,5,6,7,8,9,10,11] = [4,5,6,7,8,9]
	  val getInRangeT2 = getInRange ~5 5 [~10,~5,0,5,10] = [0]
      val getInRangeT3 = getInRange ~1 1 [~2,2,3,4,5] = []
    in
	print("\n- - - - - - - - - - - - - -\n" ^ 
      "\n[!] - Starting getInRange() Tests\n" ^
            "  Test1: " ^ Bool.toString(getInRangeT1) ^ "\n" ^
            "  Test2: " ^ Bool.toString(getInRangeT2) ^ "\n" ^
			"  Test3: " ^ Bool.toString(getInRangeT3) ^ "\n" ^
			"[!] - Ending getInRange() Tests\n\n")		
    end;
	 val _ = getInRangeTests() 

(*
 * countInRange Tests
 *)
fun countInRangeTests() =
	let
      val countInRangeT1 = countInRange 3 10 [[1,2,3,4],[5,6,7,8,9],[10,11]] = 6
	  val countInRangeT2 = countInRange ~5 5 [[~10,~5,~4],[0,4,5],[],[10]] = 3
      val countInRangeT3 = countInRange 1 5 [[1,5],[1],[5],[]] = 0
    in
	print("\n- - - - - - - - - - - - - -\n" ^ 
      "\n[!] - Starting countInRange() Tests\n" ^
            "  Test1: " ^ Bool.toString(countInRangeT1) ^ "\n" ^
            "  Test2: " ^ Bool.toString(countInRangeT2) ^ "\n" ^
			"  Test3: " ^ Bool.toString(countInRangeT3) ^ "\n" ^
			"[!] - Ending countInRange() Tests\n\n")		
    end;
	val _ = countInRangeTests() 
	
(*
 * addLengths Tests
 *)
fun addLengthsTests() =
	let
      val addLengthsT1 = addLengths (FOOT 2) (INCH 5) = INCH 29
	  val addLengthsT2 = addLengths (YARD 3) (INCH 3) = INCH 111
      val addLengthsT3 = addLengths (FOOT 3) (FOOT 5)= INCH 96
    in
	print("\n- - - - - - - - - - - - - -\n" ^ 
      "\n[!] - Starting addLengths() Tests\n" ^
            "  Test1: " ^ Bool.toString(addLengthsT1) ^ "\n" ^
            "  Test2: " ^ Bool.toString(addLengthsT2) ^ "\n" ^
			"  Test3: " ^ Bool.toString(addLengthsT3) ^ "\n" ^
			"[!] - Ending addLengths() Tests\n\n")		
    end;
	 val _ = addLengthsTests() 

(*
 * addAllLengths Tests
 *)
 fun addAllLengthsTests() =
	let
      val addAllLengthsT1 = addAllLengths [[YARD 2, FOOT 1], [YARD 1, FOOT 2, INCH 10],[YARD 3]] = INCH 262
	  
      val addAllLengthsT3 = addAllLengths [[FOOT 2], [FOOT 2, INCH 2],[]]= INCH 50
	  val addAllLengthsT4 = addAllLengths []= INCH 0

    in
	print("\n- - - - - - - - - - - - - -\n" ^ 
      "\n[!] - Starting addAllLengths() Tests\n" ^
            "  Test1: " ^ Bool.toString(addAllLengthsT1) ^ "\n" ^
            
			"  Test2: " ^ Bool.toString(addAllLengthsT3) ^ "\n" ^
			"  Test3: " ^ Bool.toString(addAllLengthsT4) ^ "\n" ^
			"[!] - Ending addAllLengths() Tests\n\n")		
    end;
	 val _ = addAllLengthsTests()

