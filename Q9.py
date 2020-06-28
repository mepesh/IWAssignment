# 9. Write a Python program to change a given string to a new string where the first
# and last chars have been exchanged.

def changeFirstLastString(sampleString):
    returnString = sampleString[-1]+sampleString[1:-2]+sampleString[0]

    return(returnString)

print(changeFirstLastString('Subash'))
