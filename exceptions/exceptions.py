def factorial(n):
    # n! can also be define as n*(n-1)
    # calcullates n recursively
    if n <= 1:
        return 1
    else:
        # print(n / 0)
        return n * factorial(n-1)


try:
    print(factorial(900))
except (RecursionError, OverflowError):
    print("This program cannot calculate factorials that large")
except ZeroDivisionError:
    print("You cannot divide by zero!")

print(4 ** 82)
print("Program terminating")

==========================================

def get_input():
    entry = input("Enter a number: ")
    return entry


first_number = get_input()
second_number = get_input()

# if first_number is num() and second_number is num()
try:
    answer = int(first_number) / int(second_number)
    print(answer)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("You must enter only numbers! No letters!")
    
===============================================

import sys

def get_input(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number entered, please try again")
        except EOFError:
            sys.exit(1)
        finally:
            print("This clause always executes")


first_number = get_input("Please enter first number: ")
second_number = get_input("Please enter second number: ")

try:
    print("{} divided by {} is: {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("You can't divide by zero")
    sys.exit(2)
else:
    print("Division performed successfully!")
