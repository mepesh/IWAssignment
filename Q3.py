# 3. Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first char itself.

sampleString = 'restart'
returnString = sampleString[0]
replaceString = '$'

for i in range(1, len(sampleString)):
    if(sampleString[i] == sampleString[0]):
        returnString += replaceString
    else:
        returnString += sampleString[i]

print(returnString)
