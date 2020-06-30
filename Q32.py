# 32.​ Write a Python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x).

def squareDictionary(n):
    returnDic = {}
    for i in range(1,n):
        dic = {i: i*i}
        returnDic.update(dic)

    return(returnDic)


print(squareDictionary(5))
