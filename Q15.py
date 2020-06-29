# 15. Write a Python function to insert a string in the middle of a string.

def stringBetweenString(string1, string2):
    midOfString = int(len(string2)/2)
    print(string2[0:midOfString])
    returnString = string2[0:midOfString]+string1+string2[midOfString:]

    return(returnString)


print(stringBetweenString('Python', '{{}}'))
