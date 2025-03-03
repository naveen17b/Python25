
x = [1, "apple", True]

print(type(x))

print(x[0])

print(x[1])

print(x[2])


x.append('testing', 478, 'dev')

print(x)


y = x.copy(all)
print(y)

x.clear()
print(x)

y.count('testing')
print(y)

y.extend('Software test engineer')
print(y)
