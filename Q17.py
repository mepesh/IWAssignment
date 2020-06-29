#17. Write a Python program to multiplies all the items in a list.

def multiply(lst):
    multiply = 1
    for i in range(len(lst)):
        multiply*=lst[i]
    return(multiply)

print(multiply([1,2,3,8]))