# 18. Write a Python program to get the largest number from a list.
def getLargest(lst):
    max = lst[0]
    for i in range(len(lst)):
        if(lst[i]>max):
            max = lst[i]
        
    return (max)

print("Maxmium is", getLargest([1,8,4,64]))