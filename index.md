#Welcome to GitHub PI_Projects_Python Page

##My projects in Python 3

###Currently there are 3 files in Python available:

1. photos_chronologically.py : The script allows you to sort photos according to the time and date the file was created and rename them to a unified one. This can be helpful when you want to display photos collected from various devices on a smartTV using a USB flash drive.

2. header_reader.py : The script uses Selenium Webdriver and reads headers from selected websites, it can also search for them by keywords. The script is still being expanded with new functionalities.

3. factorial_3_ways.py : The script computes the factorial value for a given number in 3 ways: using the 'math' module, computing iteratively and computing recursively.

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

def giverecursfactorial(x):
    if x == 1 or x ==0 :
        return 1
    else:
        return x * giverecursfactorial(x - 1)

print(f'Factorial of {number} = ', giverecursfactorial(number))


