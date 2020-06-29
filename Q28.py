# 28. Write a Python script to add a key to a dictionary.

def addKeyToDict(dic, key):
    # print(type(dic))
    if(type(dic) == dict and type(key) == dict):
        # print(dir(dic))
        dic.update(key)
    else:
        return "Invaid Dictionary"
    
    return(dic)

print('The key has been added to Dictionary', addKeyToDict({1:2, 21:23}, {'key':'value'}))
