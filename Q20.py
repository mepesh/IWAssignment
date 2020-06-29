# 20. Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of
# strings.

def getSameFirstLast(lst):
    count = 0
    for i in range(len(lst)):
        if(len(lst[i])>2):
            testString = lst[i]
            if(testString[0] == testString[-1]):
                count += 1
    return count

print("The no of same charcters strings in the list is ", getSameFirstLast(['apple','rar','lol']))
