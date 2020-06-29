# 26. Write a Python program to insert a given string at the beginning of all items in
# a list.

def appendStringInListItems(lst , string):
    returnString = []
    for i in range(len(lst)):
        returnString.append(string + str(lst[i]))
    
    return(returnString)

print("List Returend is", appendStringInListItems([1,2,3,4], 'event'))