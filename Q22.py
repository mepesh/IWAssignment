# 22. Write a Python program to remove duplicates from a list.

def removeDuplicate(lst):
    returnList = list(dict.fromkeys(lst))
    return (returnList)

print("Removed Duplicate",removeDuplicate([1,1,5,2]))
    
    