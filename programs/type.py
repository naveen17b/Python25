# string input
#intro to the types and the input function

input_a = input('Enter a string: ')

 # print type
print(type(input_a))

# integer input
input_b = int(input('enter an integer: '))

# print type
print(type(input_b))

#try and except block to handle the exception 

try:
    input_a = int(input('Enter some characters '))
    if input_a.isdigit():
         
     print(type(input_a))

except ValueError:

      # print type
      print('please enter an integer')
