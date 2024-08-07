# Sets
* A set is an unordered collection of unique elements. It is one of the four built-in data types in Python, alongside lists, tuples, and dictionaries
* Sets are written with curly braces {}. For example:
* myset = {"apple", "banana", "cherry"}
* Sets are unordered, so the order of items is not guaranteed. 
* Set items are unchangeable (immutable), but you can add or remove items. 
* Sets do not allow duplicate values.
* thisset = {"apple", "banana", "cherry"} 
* print(len(thisset))  # Get the number of items in the set
* Sets can contain elements of any data type (e.g., strings, integers, booleans).
* You can create a set using the set() constructor:
* thisset = set(("apple", "banana", "cherry"))  # Note the double round-brackets

# Sets Methods
* Adding Element
* Removing Element
* Emptying The Sets
* determining Set Size
* Checking Membership
* Set Operations

## Adding Element:- 
* To add an element to a set, use the add() method:
* my_set = {1, 2, 3} 
* my_set.add(4)  # Adds 4 to the set

## Removing Elements:
* Use the remove() method to remove a specific element (raises an error if the element is not found).
* my_set.remove(2)  # Removes 2 from the set
* Alternatively, use the discard() method (doesn’t raise an error if the element is not found):
* my_set.discard(3)  # Removes 3 from the set

## Emptying the Set:
* Clear all elements from a set using the clear() method:
* my_set.clear()  # Removes all elements from the set

## Determining Set Size:
* Get the number of elements in a set using the len() function:
* size = len(my_set)  # Returns the size of the set

## Checking Membership:
* Use the in keyword to check if an element is present in the set:
* if 4 in my_set:
* print("4 is in the set")

## Set Operations:
* Combine sets using methods like:
* union(): Returns a new set with elements from both sets.
* intersection(): Returns a new set with common elements.
* difference(): Returns a new set with elements in the first set but not the second.
* symmetric_difference(): Returns a new set with elements in either set but not both.

## Union of Sets (A ∪ B):
* The union of two sets, A and B, contains all distinct elements from both sets.
* In Python, you can use the | operator or the .union() method to perform the union.
* Example:
* A = {1, 2, 3}
* B = {3, 4, 5}
* union_result = A | B  # Using the '|' operator
* Result: {1, 2, 3, 4, 5}

## Intersection of Sets (A ∩ B):
* The intersection of sets A and B contains common elements present in both sets.
* In Python, you can use the & operator or the .intersection() method.
* Example:
* A = {1, 2, 3}
* B = {3, 4, 5}
* intersection_result = A & B  # Using the '&' operator 
* Result: {3}

## Set Difference (A - B):
* The difference between sets A and B includes elements in A but not in B.
* In Python, you can use the - operator or the .difference() method.
* Example:
* A = {1, 2, 3} 
* B = {3, 4, 5} 
* difference_result = A - B  # Using the '-' operator 
* Result: {1, 2}

## Symmetric Difference (A ⊕ B):
* The symmetric difference between sets A and B contains elements in either set but not both.
* In Python, you can use the ^ operator or the .symmetric_difference() method.
* Example:
* A = {1, 2, 3}
* B = {3, 4, 5}
* symmetric_difference_result = A ^ B  # Using the '^' operator 
* Result: {1, 2, 4, 5}





