# 4. Create a list. Append the names of your colleagues and friends to it.
# Has the id of the list changed? Sort the list. What is the first item on
# the list? What is the second item on the list?

sampleList = ['Dipesh','Butwal']
print(id(sampleList))
sampleList.append('My Friend')
print(id(sampleList))
sampleList.sort()
print(sampleList)