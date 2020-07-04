# 5.​ Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.

def findFactorial(number):
    factorial = 1
    for i in range(1, number+1):
        factorial *= i
    return(factorial)


print('Factorial is:', findFactorial(3))

# 6.​ Write a Python function to check whether a number is in a given range.


def findInRange(start, end, number):
    present = False
    for i in range(start, end):
        if(i == number):
            present = True

    return (present)


print(f'Number Present in Range: ', findInRange(25, 32, 27))

# 7.​ Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.


def countUpperLower(string):
    count = {'upper': 0, 'lower': 0}
    for i in range(len(string)):
        if string[i].isupper():
            count['upper'] += 1
        else:
            count['lower'] += 1
    return count


count = countUpperLower('LoWerCasesareCrap')
print('No of UpperCasse ', count.get('upper'))
print('No of Lower Cases', count.get('lower'))

# 8.​ Write a Python function that takes a list and returns a new list with unique
# elements of the first list.


def getUniqueList(lst):
    return list(dict.fromkeys(lst))


lst = [1, 3, 3, 3, 4, 8, 4]
print(getUniqueList(lst))

# 9.​ Write a Python function that takes a number as a parameter and check the
# number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that
# has no positive divisors other than 1 and itself.


def checkPrime(num):
    if(num < 1):
        return ("CAnnot take negative inputs")
    elif(num == 1):
        return ("Is a Nor a Prime or Composite")
    else:
        for i in range(2, num):
            if(num % i == 0):
                return(f'{num} is Composite')
        return (f'{num} is Prime')


print(checkPrime(29))

# 12.​ Write a Python program to create a function that takes one argument, and
# that argument will be multiplied with an unknown given number.

def randomMultiply(num):
    multiplier = 16
    return (multiplier*num)

print('The Random multiplied is', randomMultiply(8))



