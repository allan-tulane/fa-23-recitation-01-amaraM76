"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
from numpy import sort
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1


def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
	if left <= right:
		middle = left + (right - left) // 2
		if mylist[middle] == key:
			return middle
		elif mylist[middle] < key:
			return _binary_search(mylist, key, middle + 1, right)
		else:
			return _binary_search(mylist, key, left, middle - 1)
	else:
		return -1

	
	"""
	Recursive implementation of binary search.

	Params:
	  mylist....list to search
	  key.......search key
	  left......left index into list to search
	  right.....right index into list to search

	Returns:
	  index of key in mylist, or -1 if not present.
	"""
	### TODO

	###




def time_search(search_fn, mylist, key):
	start = time.time() * 1000 
	search_fn(mylist, key)
	end = time.time() * 1000
	totalTime = start - end 
	return totalTime		

	"""
	Return the number of milliseconds to run this
	search function on this list.

	Note 1: `sort_fn` parameter is a function.
	Note 2: time.time() returns the current time in seconds. 
	You'll have to multiple by 1000 to get milliseconds.

	Params:
	  sort_fn.....the search function
	  mylist......the list to search
	  key.........the search key 

	Returns:
	  the number of milliseconds it takes to run this
	  search function on this input.
	"""
	### TODO

	###

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	key = -1 
	results = []
	for x in sizes:
		n = int(x)
		mylist = list(range(n)) 
		linear_search_time = time_search(linear_search, mylist, key)
		binary_search_time = time_search(binary_search, mylist, key)
		results.append((n, linear_search_time, binary_search_time))

	return results
	"""
	Compare the running time of linear_search and binary_search
	for input sizes as given. The key for each search should be
	-1. The list to search for each size contains the numbers from 0 to n-1,
	sorted in ascending order. 

	You'll use the time_search function to time each call.

	Returns:
	  A list of tuples of the form
	  (n, linear_search_time, binary_search_time)
	  indicating the number of milliseconds it takes
	  for each method to run on each value of n
	"""
	### TODO

	###

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))
results = compare_search()
print_results(results)
