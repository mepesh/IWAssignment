# 2.Write a Python program to get a string made of the first 2 and the last 2 chars
# from a given a string. If the string length is less than 2, return instead of the
# empty string.

sampleString = 'Python'
stringLength = len(sampleString)

if(stringLength < 2):
    returnString = ''
else:
    returnString = sampleString[0]+sampleString[1] + \
        sampleString[stringLength-2]+sampleString[stringLength-1]

print(returnString)
