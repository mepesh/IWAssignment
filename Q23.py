# 23. Write a Python program to check a list is empty or not.

def checkEmpty(lst):
    if(len(lst) == 0):
        return ("Empty List")
    else:
        return("Non empty List")

print(checkEmpty([]))