# 29. Write a Python script to concatenate following dictionaries to create a new
# one.

def conDictionaries(*args):
    for i in range(1, len(args)):
        args[0].update(args[i])

    return(args[0])


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

print('The concatinated dictionary', conDictionaries(dic1, dic2, dic3))
