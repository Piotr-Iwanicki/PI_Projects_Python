# Factiorial in 3 ways

import math

number = (input("Enter a number to calculate the factorial: "))

if not number.isdigit():
    print("Sorry, number must be an integer !")
    print(f"Input is digit? - {number.isdigit()}")
    exit()

number = int(number)
print("")

control_result = math.factorial(number)
print(f'*Control result, factorial of {number} = {control_result}')
print("")
print("*By iteration")


def GiveFactorial(number):
    if number == 1 or number == 0:
        return print(f'Factorial of {number} = {1}')
    else:
        fact = number
        for i in range(fact - 1):
            fact = fact * (i + 1)
        return print(f'Factorial of {number} = {fact}')


GiveFactorial(number)
print("")
print("*By recursion")


# n! = n * (n-1)!

def giverecursfactorial(x):
    if x == 1 or x ==0 :
        return 1
    else:
        return x * giverecursfactorial(x - 1)


print(f'Factorial of {number} = ', giverecursfactorial(number))
