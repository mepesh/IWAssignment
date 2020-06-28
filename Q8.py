# 8. Write a Python program to remove the nth
# index character from a nonempty string.

def removeNthIndex(sampleString, position):
    beforeNth = sampleString[:position]
    afterNth = sampleString[position+1:]
    return(beforeNth+afterNth)


print(removeNthIndex('nonempty', 5))
