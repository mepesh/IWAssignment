# 6. Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

myFriendList = ['Ram', 'John', 'Lenon', 'Avici']


def johnFinder(lst, name):
    for i in range(len(myFriendList)):
        if(myFriendList[i] == name):
            return f'{name} Found'

    return f'not found'


print(johnFinder(myFriendList, 'John'))
