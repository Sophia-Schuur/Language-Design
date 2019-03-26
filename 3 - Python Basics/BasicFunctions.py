'''Sophia Schuur
3/3/2019
Basic python practice for learning. Performs handful of independent functions.
Includes Lists, dictionaries, loops, tuples, classes, higher-order functions and iterator practice.'''


from functools import reduce
from itertools import combinations

'''Input: dictionary. Maps bus routes to bus stops.
   Output: dictionary. Maps bus stops to bus routes that stop at that stop. Alphabetically sorted.'''
def busStops(b):
	ret = {}
	stops = []
	for bus in b:				# each bus route (key) and its list of stops		
		stops = b[bus]			# put each stop into new list stops
		
		for stop in stops:		# for each individual stop in list stops
			if stop not in ret:			# if the stop does not exist in ret
				ret[stop] = [bus]			# map key at this current stop to current bus route
			else:
				newStops = ret[stop]	
				newStops.append(bus)	# add current bus route key to newStops
				newStops.sort()			# sort alpabetically

	return ret

def testbusStops():
	buses = {
		"Lentil": ["Chinook", "Orchard", "Valley", "Emerald","Providence", "Stadium", "Main", "Arbor", "Sunnyside", "Fountain", "Crestview", "Wheatland", "Walmart", "Bishop", "Derby", "Dilke"],
		"Wheat": ["Chinook", "Orchard", "Valley", "Maple","Aspen", "TerreView", "Clay", "Dismores", "Martin", "Bishop", "Walmart", "PorchLight", "Campus"],
		"Silver": ["TransferStation", "PorchLight", "Stadium", "Bishop","Walmart", "Shopco", "RockeyWay"],
		"Blue": ["TransferStation", "State", "Larry", "TerreView","Grand", "TacoBell", "Chinook", "Library"],
		"Gray": ["TransferStation", "Wawawai", "Main", "Sunnyside","Crestview", "CityHall", "Stadium", "Colorado"]}

	if busStops({}) != {}:
		return False
	if busStops(buses) != {'Chinook': ['Blue', 'Lentil', 'Wheat'], 'Orchard': ['Lentil', 'Wheat'], 'Valley': ['Lentil', 'Wheat'], 'Emerald': ['Lentil'], 'Providence': ['Lentil'], 'Stadium': ['Gray', 'Lentil', 'Silver'], 'Main': ['Gray', 'Lentil'], 'Arbor': ['Lentil'], 'Sunnyside': ['Gray', 'Lentil'], 'Fountain': ['Lentil'], 'Crestview': ['Gray', 'Lentil'], 'Wheatland': ['Lentil'], 'Walmart': ['Lentil', 'Silver', 'Wheat'], 'Bishop': ['Lentil', 'Silver', 'Wheat'], 'Derby': ['Lentil'], 'Dilke': ['Lentil'], 'Maple': ['Wheat'], 'Aspen': ['Wheat'], 'TerreView': ['Blue', 'Wheat'], 'Clay': ['Wheat'], 'Dismores': ['Wheat'], 'Martin': ['Wheat'], 'PorchLight': ['Silver', 'Wheat'], 'Campus': ['Wheat'], 'TransferStation': ['Blue', 'Gray', 'Silver'], 'Shopco': ['Silver'], 'RockeyWay': ['Silver'], 'State': ['Blue'], 'Larry': ['Blue'], 'Grand': ['Blue'], 'TacoBell': ['Blue'], 'Library': ['Blue'], 'Wawawai': ['Gray'], 'CityHall': ['Gray'], 'Colorado': ['Gray']}:
		return False
	return True

'''Input: Dictionary. Maps days of week to classes and hours studied for each. 
	Output: Dictionary. Maps each class to total hours studied.'''
def addDict(d):
	ret = {}
	# get each day of week
	for day, classes in d.items():				# day: Mon, Tue, etc; classes: dictionary of classes
		# get each study hour per lecture
		for lecture, hours in classes.items():	# lecture: 355, etc; hours: int studied
			if lecture in ret.keys():	# does the lecture already exist?
				ret[lecture] += hours	# if yes, add hours to lecture in ret
			else:
				ret[lecture] = hours	# if not, make a new lecture entry in ret
	return ret

def testaddDict():
    d = {'Mon':{'355':2,'451':1,'360':2},'Tue':{'451':2, '360':3}, 'Thu':{'355':3,'451':2,'360':3}, 'Fri':{'355':2}, 'Sun':{'355':1,'451':3,'360':1}}
    if addDict({}) != {}:
        return False
    if addDict(d) != {'355': 8, '360': 9, '451': 8}:
        return False
    return True


'''Input: List of Dictionaries. Maps days of week to classes and hours studied for each for each WEEK
	Must use map and reduce.
	Output: Dictionary. Maps each class to total hours studied.'''
def addDictN(L):
	
	if L == {}:		#empty L?
		return {}		#return an empty dictionary
	else:			#if L not empty, continue with function
		dictMap = list(map(addDict, L))	# do addDict to each dictionary in list (each week)	
		def addDictNHelper(L1, L2):	# Used by reduce to add each list to each other i.e week1 + week2 + ... + weekn

			for lecture in L2:					# each lecture in L2
				if lecture not in L1:			# does the lecture exist in L1?
					L1[lecture] = L2[lecture]		# if not, add lecture to L2 
				else:
					L1[lecture] += L2[lecture]		#if yes, add lecture and hours
			return L1		
		ret = reduce(addDictNHelper, dictMap)
		return ret

def testaddDictN():
	d = [{'Mon':{'355':2,'360':2},'Tue':{'451':2,'360':3},'Thu':{'360':3}, 'Fri':{'355':2}, 'Sun':{'355':1}},{'Tue':{'360':2},'Wed':{'355':2},'Fri':{'360':3, '355':1}},{'Mon':{'360':5},'Wed':{'451':4},'Thu':{'355':3},'Fri':{'360':6}, 'Sun':{'355':5}}]
	d2 = [{'Mon':{'sandwich':2,'pork':1},'Tue':{'soup':1,'steak':1},'Thu':{'eggs':3}, 'Fri':{'steak':1}, 'Sun':{'soup':1}},{'Tue':{'sandwich':3},'Wed':{'pork':1},'Fri':{'eggs':4, 'sandwich':3}},{'Mon':{'pork':2},'Wed':{'steak':4},'Thu':{'soup':1},'Fri':{'soup':2}, 'Sun':{'steak':2}}]
	
	if addDictN(d2) != {'sandwich': 8, 'pork': 4, 'soup': 5, 'steak': 8, 'eggs': 7}:
		return False

	if addDictN({}) != {}:
		return False
	if addDictN(d) != {'355': 16, '360': 24, '451': 6}:
		return False
	return True


'''Input: List of dictionaries (L), key (k).
	Checks each dictionary in L for k in REVERSE. If k occurs > once, returns first value seen.
	Output: value at k'''
def searchDicts(L, k):
	for d in reversed(L):
		for l in d.items():
			#print(l)
			if k in l:
				return l[1]
			else:
				pass

def testsearchDicts():
	L1 = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]

	if searchDicts(L1, "tunasalad") != None:
		return False
	if searchDicts([{}], "") != None:
		return False

	if searchDicts(L1,"x") != 2:
		return False
	if searchDicts(L1,"y") != False:
		return False
	if searchDicts(L1,"z") != "found":
		return False
	if searchDicts(L1,"t") != None:
		return False
	return True

	
'''Input: List of tuples tL, key k
	Starts from end of list. Checks dictionary in each tuple following the index specified in the tuples.
	Output: value at k'''
def searchDicts2(tL, k):
	if tL == [()]:		#empty tL?
		return [()]		#return empty list of tuples
	else:	
	#tL[i = tuple index][0,1 = either int index or dictionary][k = index of item in dictionary]
		def searchDicts2Helper(i, tL, k):
		    if k in tL[i][1]:		# key in current dictionary (tL[i][1]?
		        return tL[i][1][k] 	# return value of k
	 
		    elif i != 0:			# not in first tuple? Keep going thru list
		        i = tL[i][0]
		        return searchDicts2Helper(i, tL, k) 

		    elif i == 0:				# first tuple in list?
		        if k in tL[i][1]:		# if k exists in dictionary
		            return tL[i][1][k] 		# return value of k
		        else:					# if k does not exist in dictionary
		            return None				# return None
		    
		    else:
		        return None 			# failsafe
		
		index = -1 						# begin at last tuple in list
		return searchDicts2Helper(index, tL, k)

def testsearchDicts2():
	L2= [(0,{"x":0,"y":True,"z":"zero"}), (0,{"x":1}),(1,{"y":False}), (1,{"x":3, "z":"three"}),(2,{})]
	
	if searchDicts2(L2, "tunasalad") != None:
		return False
	if searchDicts2([()], "") != [()]:
		return False

	if searchDicts2 (L2,"x") != 1:
		return False
	if searchDicts2 (L2,"y") != False:
		return False
	if searchDicts2 (L2,"z") != "zero":
		return False
	if searchDicts2 (L2,"t") != None:
		return False

	return True



'''Input: List.
	Output: List of Lists where each sublist is one of the 2^(length(L)) subsets of L. Increasing length.'''
def subsets(L):
	ret = [[]]
	length = len(L) + 1
		# combinations(p, r): returns r-length tuples, in sorted order, no repeated elements
		# sum(iterable, start): adds start and items of the given iterable from left to right
	innerMap = sum(map(lambda combo: list(combinations(L, combo)), range(1, length)), [])	#do combo() on all sublists of L
	outerMap = map(list, innerMap)	#make sublists a list of lists instead of seperate tuples
	return ret + list(outerMap)		#gotta return a list


def testsubsets():
	if(subsets([3, 6, 9])) != [[],[3],[6],[9],[3,6],[3,9],[6,9],[3,6,9]]:
		return False
	if(subsets([2, 4, 6, 8])) != [[], [2], [4], [6], [8], [2, 4], [2, 6], [2, 8], [4, 6], [4, 8], [6, 8], [2, 4, 6], [2, 4, 8], [2, 6, 8], [4, 6, 8], [2, 4, 6, 8]]:
		return False

	if subsets([1,2,3]) != [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]:
		return False
	if subsets([(1,"one"),(2,"two")]) != [[],[(1,"one")],[(2,"two")],[(1,"one"),(2,"two")]]:
		return False
	if subsets([]) != [[]]:
		return False
	return True



'''Input: length of grid m, width n.
	Output: number of different paths one can take from start (0,0; top left) to end (M-1, N-2; bottom right)'''
def numPaths(m, n):
	if(m == 1 or n == 1):		#1x1 path just returns 1
		return 1
	elif(m == 0 and n == 0):	# Cannot have no grid squares, causes stack error. Just return 0 as an error check.
		return 0
	else:
		return numPaths(m-1, n) + numPaths(m, n-1)

def testnumPaths():

	if numPaths(0,0) != 0:
		return False
	if numPaths(8,8) != 3432:
		return False

	if numPaths(2,2) != 2:
		return False
	if numPaths(3,3) != 6:
		return False
	if numPaths(4,5) != 35:
		return False
	return True


'''Iterator representing the sequence of primes starting from 2.'''
class iterPrimes:
	def __init__(self):
		self.current = 1

	def __next__(self):
		self.current = self.current + 1
		
		while 1:	# check for primes
			for i in range(2, self.current // 2 + 1):
				if self.current % i == 0:
					self.current = self.current + 1
					break 		# exit for loop
			else:
				break 			# exit while loop
		return self.current

	def __iter__(self):
		return self

'''Input: Sequence of positive ints iNumbers, positive int sum
	Output: Next n elements from iNumbers such that the next n elements of the iterator 
		add to <sum but the next (n + 1) elements of the iterator add to >=sum.'''
def numbersToSum(iNumbers, sum):
	ret = []
	count = 0
	primes = iterPrimes()
	primes.__next__()

	for n in iNumbers:
		if (count + n > sum):		# cant have sequence > sum ever
			break
		elif (count + n < sum):		# if current seqeuence < sum, add this element to return list
			ret.append(n)
			count += n
			if (count + primes.__next__() >= sum):	#cant have next iterator >= sum
				break
	return ret

def testnumbersToSum():
    primes = iterPrimes()
    if numbersToSum(primes, 58) != [2, 3, 5, 7, 11, 13]:
        return False
    if numbersToSum(primes, 100) != [17, 19, 23, 29]:
         return False
    return True


testFunctions = {"busStops":testbusStops,  "addDict": testaddDict, "addDictN": testaddDictN, "searchDicts": testsearchDicts, "searchDicts2": testsearchDicts2, "subsets":testsubsets, "numPaths": testnumPaths, "numbersToSum":testnumbersToSum  }
if __name__ == "__main__":
	for testName,testFunc in testFunctions.items():
		print(testName,':  ',testFunc())
		print('---------------------')

	
