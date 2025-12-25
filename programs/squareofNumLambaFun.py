
''' sqares of range of numbers using lambda function '''

squares =[]
for i in range (10):
    squares.append(i**2)

square_lamba = list (map (lambda x: x**2, range (10)))

print("squares using for loop :", squares)
print("squares using lambda function :", square_lamba)


