# 30.​ Write a Python script to check whether a given key already exists in a
# dictionary.

def checkKeysDict(dic, checkKey):
    exist = False
    for key in dic.keys():
        if(key == checkKey):
            exist = True
            break
    return exist


print('The key is present in the dict: ', checkKeysDict(
    {1: 2, 'apple': 'fruit'}, 'a'))
