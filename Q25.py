# 25. Write a Python program to check whether all dictionaries in a list are empty or
# not.

def checkEmpty(args):
    empty = True
    for i in args:
        if type(i) == dict:
            if(len(i)!=0):
                empty = False
        else:
            pass
    
    return empty

print("The input list is ", checkEmpty([{2:3},65,{'apple',"testy"},{}]))   
print("The input list is ", checkEmpty([5,{},{}]))         