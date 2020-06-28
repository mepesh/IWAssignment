# 10. Write a Python program to remove the characters which have odd index
# values of a given string.

def removeOddIndex(inputString):
    returnString = ''
    for i in range(len(inputString)):
        if (i % 2 == 0):
            returnString += inputString[i]
        

    return(returnString)


print(removeOddIndex('calculator'))
