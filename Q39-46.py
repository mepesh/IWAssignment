# 39.​ Write a Python program to unpack a tuple in several variables.

sampleTuple = {1, 2, 3, 4}

x, y, z, k = tuple(sampleTuple)

print(z)

# 40.​ Write a Python program to add an item in a tuple.


def addItemTuple(tuple, item):
    tuple.add(item)
    return tuple


print(addItemTuple(sampleTuple, 65))

# 41.​ Write a Python program to convert a tuple to a string.

def tupleToString(tuple):
    return (str(tuple))

print(type(tupleToString(sampleTuple)))

# 42.​ Write a Python program to convert a list to a tuple.

def listToTuple(lst):
    returnTuple = tuple(lst)
    print(type(returnTuple))

    return(returnTuple)

sampleList = [1,2,3]
print(listToTuple(sampleList))

#43.​ Write a Python program to remove an item from a tuple.

def removeFromTuple(tuple, item):
    tuple.remove(item)
    return tuple

print(removeFromTuple(sampleTuple,2))

#44.​ Write a Python program to slice a tuple

def sliceTuple(tpl, start, end):
    print(tpl[2:3])

    # return returnTuple

tuple2 = (6,4,8,9,78)
print('Sliced tuple is: ', sliceTuple(tuple2, 2,3))

# 45.​ Write a Python program to find the index of an item of a tuple.
def findIndex(tuple2, item):
    index = tuple2.index(item)
    return index

item = 8
print(f'Index of {item} in {tuple2} is ', findIndex(tuple2, item))

#46.​ Write a Python program to find the length of a tuple

def lengthOfTuple(tuple2):
    length = len(tuple2)
    return length

print (f'The length of {tuple2} is ', lengthOfTuple(tuple2))
