character = input('Enter some character :')

''' 
#.isdigit() is a string method. 
It returns True if all the characters are digits, otherwise False.

'''
if character.isdigit():  
    character =int(character)   
    if character<0:
        print('the input fed is a negative number')
    elif character %2 ==0:
        print('the input fed is an even number')
    elif character %2 !=0:
        print('the input fed is an odd number')
else:
    print('please enter an integer')

