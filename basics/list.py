"""list data type in python
- ordered collection of items
- allows duplicate values
- mutable (can be changed after creation)"""

x = [1, "apple", True]

print(type(x))

print(x[0])

print(x[1])

print(x[2])

"""
append:
# append adds new element to the list, and it will be added at the end of the list
# it taskes only one element at a  time
"""

x.append("testing")
print(x)

y = x.copy()
print(y)

x.clear()
print(x)

y.count("testing")
print(y)

# y.extend('Software test engineer')
# print(y)

""" insert method adds element at specified index
    syntax : list_name.insert(index, element) 
    
    """

y.insert(3, "automation")
print("list item in y :", y)


""" Remove method removes element at specified index
    syntax : list_name.pop(index)"""

removed_item = y.pop(0)
print("Removed item: ", removed_item)
print("List after popping element: ", y)


""" reverse method reverses the order of elements in the list
    syntax : list_name.reverse()
"""
y.reverse()
print("Reversed List y: ", y)

""" is operator in list
    used to check whether two lists are same or not (based on memory location)
    syntax : list1 is list2 
"""
z = [1, 2, 3, 4, 5]
a = [1, 2, 3, 4, 5]

print(z is a) 
# false because both are different objects in memory

""" 
extends method in list
# extend method adds elements of one list to another list
"""

a = [75, 80, 85, 48, 85, 96, 100, 55, 85]
a.extend([45, 60, 78])
print(a)

""" count method in list
# count method returns the number of occurrences of an element in the list
"""
print(a.count(85))


""" sort method in list
# sort method sorts the elements of the list in ascending order"""

print(a.sort())

""" clear method in list
# clear method removes all elements from the list
"""

print(a.clear())

