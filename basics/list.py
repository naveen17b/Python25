
x = [1, "apple", True]

print(type(x))

print(x[0])

print(x[1])

print(x[2])

# append adds new element to the list, and it will be added at the end of the list
# it taskes only one element at a  time
x.append('testing')

print(x)


y = x.copy()
print(y)

x.clear()
print(x)

y.count('testing')
print(y)

# y.extend('Software test engineer')
# print(y)

y.insert(3,'automation')
print(y)


x = [1, 2, 3, 4, 5]
y = [1,2,3,4,5]

print(x is y)  # false because both are different objects in memory