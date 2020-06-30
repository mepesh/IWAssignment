# 34.​ Write a Python script to merge two Python dictionaries.

def mergeDic(dic1, dic2):
    dic1.update(dic2)
    print(dic1)

    return (dic1)


dic1 = {'vehicle': 'suzuki', 'fruit': 'apple'}
dic2 = {'name': 'Dipesh', 'address': 'Butwal'}

print('Merge Dictionary', mergeDic(dic1, dic2))
