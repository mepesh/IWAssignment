# 10. Write a function that takes camel-cased strings (i.e.
# ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument,
# separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.

def convertCamelCase(str, seprator):
    returnString = ''
    for i in range(len(str)):
        if(i==0 and str[i].isupper()):
            returnString+=str[i].lower()

        elif (i>0 and str[i].isupper()):
            returnString+= seprator
            returnString+=str[i].lower()
            
        else:
            returnString+=str[i]

    return returnString

print(convertCamelCase('ThisIsFun', "-"))