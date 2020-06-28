# 5. Write a Python program to add 'ing' at the end of a given string (length should
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
# string length of the given string is less than 3, leave it unchanged.

sampleString = 'sleeping'
stringLength = len(sampleString)
returnString = ''

if(stringLength < 3):
    returnString = sampleString
else:
    indentString = sampleString[stringLength-3] + \
        sampleString[stringLength-2]+sampleString[stringLength-1]
    print(indentString)
    if(indentString == 'ing'):
        returnString = sampleString+'ly'
    else:
        returnString = sampleString+'ing'

print(returnString)
