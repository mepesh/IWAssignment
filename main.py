# 1. Write a Python program to count the number of characters (character
# frequency) in a string. Sample String : google.com'

string = 'google.com'
count ={}
print(type(count))
for i in range(len(string)):
    key = string[i]
    # value = 1
    if key in count:
        count[key]= count[key]+1
    else:
        count[key]=1

print(count)