try:
    num = int(input("Enter a number: "))
    print(num / 2)

except ZeroDivisionError:
    print("Cannot divide by zero.")

    # except ValueError:
# print("That was not a valid number.")
