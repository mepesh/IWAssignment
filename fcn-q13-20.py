# 13.​ Write a Python program to sort a list of tuples using Lambda.


def sortList(lst):
    lst.sort(key=lambda x: x[0])
    return lst


lstTuple = [(1, 2, 3), (65, 28), (0, 99)]
print(sortList(lstTuple))

# 14.​ Write a Python program to sort a list of dictionaries using Lambda.


def sortDictionaryList(lst):
    lst.sort(key=lambda x: x['name'])
    return lst


lstDic = [{'name': 'Dipesh', 'class': 10}, {'class': 9, 'name': 'Ramesh'}]
print(sortDictionaryList(lstDic))

# 15.​ Write a Python program to filter a list of integers using Lambda.


def filterList(lst):
    lst = list(filter(lambda x: (x % 2 == 0), lst))
    return lst


sampleList = [1, 8, 2, 6, 9]
print('Filter the even in list', filterList(sampleList))

# 16.​ Write a Python program to square and cube every number in a given list of
# integers using Lambda.


def powerFcn(lst, power):
    if(power == 'square'):
        powerList = list(map(lambda x: x*x, lst))
    elif(power == 'cube'):
        powerList = list(map(lambda x: x*x*x, lst))
    return powerList


print(powerFcn(sampleList, 'cube'))

# 17.​ Write a Python program to find if a given string starts with a given character
# using Lambda.

sampleString = 'apple'
character = 'a'
def hasCharacter(x, y): return True if(x[0] == y) else False


print(hasCharacter(sampleString, character))

# 18.​ Write a Python program to check whether a given string is number or not
# using Lambda.


def checkNumber(x): return True if((float(x)).is_integer()
                                   ) else (False if ValueError else False)


print(checkNumber('5'))

# 19.​ Write a Python program to create Fibonacci series upto n using Lambda.


def fibonacci(number):
    fibonachiList = [0, 1]
    if(number <= 0):
        return fibonachiList[0]
    else:
        for i in range(2, number):
            print(i)
            fibonachiList.append(fibonachiList[i-1]+fibonachiList[i-2])

    return fibonachiList


print(fibonacci(10))

# 20. Write a Python program to find intersection of two given arrays using
# Lambda.

array1 = [1, 2, 3]
array2 = [3, 4, 6]
print(type(array1))

intersection = lambda x,y: set(x) & set(y)
print(list(intersection(array1,array2)))