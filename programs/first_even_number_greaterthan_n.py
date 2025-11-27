# find the first even number greater than 10

for i in range(30,30):  # creates an empty range, so it never executes and prints nothing
    if i % 2 == 0:
        print(i)
        break


# find the first even number greater than n

def first_even_number_greater_than_n(n):
    for i in range(n+1, n+10):
        if n%2==0:
            return n+2
        else:
            return n+1

print(first_even_number_greater_than_n(1012))
print(first_even_number_greater_than_n(1523))        
