# 24. Write a Python program to clone or copy a list.

def copyList(lst):
    copyList = lst.copy()
    return(copyList)

newList = copyList(['apple','ball'])
print('The new list is ', newList)