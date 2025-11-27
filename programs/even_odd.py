
#seperate the even and odd numbers from the list
list=[2,4,7,1,5,10]
even_numbers=[]
odd_numbers=[]

for ev in list:
    if ev%2 ==0:
        even_numbers.append(ev)
    else:
        odd_numbers.append(ev)
        
print("Even numbers are:", even_numbers.sort)
print("Odd numbers are:", odd_numbers)

