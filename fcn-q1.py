# 1.​ Write a Python function to find the Max of three numbers.

def getMax(*args):
    print(type(args))
    return(max(args))

print("Max of the input is: ",getMax(1,0,25))