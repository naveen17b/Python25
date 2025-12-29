"""
Sets in Python are unordered collections of unique, 
immutable elements, ideal for storing data without duplicates. 
They belong to Python's four main collection types alongside lists, 
tuples, and dictionaries, but stand out for automatically 
eliminating repeated items.
"""

commonSet = {1, "apple", True}
print(type(commonSet)) 

commonSet.add("Testing")
print(commonSet)

commonSet.remove(1)
print(commonSet)

commonSet.update(["QA", "Developer", "DevOps"])
print(commonSet)

# commonSet[0] = "New Value"  # This will raise an error since sets are unordered and do not support indexing

commonSet.discard("apple")
print(commonSet)

# Demonstrating set operations
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
print("Union:", setA | setB)            # Union
print("Intersection:", setA & setB)     # Intersection
print("Difference:", setA - setB)       # Difference
print("Symmetric Difference:", setA ^ setB)  # Symmetric Difference
print("Is setA a subset of setB?", setA <= setB)  # Subset check
print("Is setA a superset of setB?", setA >= setB)  # Superset check
print("Are setA and setB disjoint?", setA.isdisjoint(setB))  # Disjoint check

# Looping through a set
for item in commonSet:
    print(item) 


""" frozenset:
A frozenset is an immutable version of a set, 
meaning its elements cannot be changed after creation.
This makes frozensets hashable and suitable for use as keys in 
dictionaries or elements of other sets.
"""
# Frozenset example
frozenSet = frozenset([1, 2, 3, 4])
print("Frozenset:", frozenSet)
# frozenSet.add(5)  # This will raise an error since frozensets are immutable
print("Is 2 in frozenSet?", 2 in frozenSet)


