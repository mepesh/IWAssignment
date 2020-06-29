#19. Write a Python program to get the smallest number from a list.

def getSmallest(lst):
    smalllest = lst[0]
    for i in range(len(lst)):
        if lst[i]<smalllest:
            smalllest = lst[i]
    
    return (smalllest)

print("Smallest in the list is: ", getSmallest([1,0,8,96]))