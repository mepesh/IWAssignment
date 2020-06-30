# 36.​ Write a Python program to sum all the items in a dictionary.
dic = {'salary': 12500, 'bonus': 8500, 'incentives': 4500}


def sumDict(dic):
    sum = 0
    for values in dic.values():
        sum += values

    return(sum)

# 37.​ Write a Python program to multiply all the items in a dictionary.


def mulDict(dic):
    mul = 1
    for values in dic.values():
        mul *= values

    return mul

# 38.​ Write a Python program to remove a key from a dictionary.


def removeKeyDic(dic, delKey):
    if delKey in dic:
        del dic[delKey]

    return dic


# print('Sum of Values in Dictionary :', sumDict(dic))
# print('Mulitply of Values in Dictionary :', mulDict(dic))
print(removeKeyDic(dic, 'salary'))
