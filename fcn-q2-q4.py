# 2.​ Write a Python function to sum all the numbers in a list.
sampleList = [1, 2, 25, 8]


def Sum(lst):
    return sum(lst)


print('Sum is ', sum([1, 2, 8]))

# 3.​ Write a Python function to multiply all the numbers in a list.


def multiply(lst):
    result = 1
    print(type(lst))
    for i in range(len(lst)):
        result = result * lst[i]
        print(result, i)

    return (result)


print('Multiply is', multiply(sampleList))

# 4.​ Write a Python program to reverse a string.


def reverseString(string):
    reverseString = ''
    for i in range(len(string)):
        reverseString+=string[-1-i]
        
    return(reverseString)

print('Reverse String ', reverseString('Dipesh'))
