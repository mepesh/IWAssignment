# 5. Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.

myTuple = ('Dipesh', 'Pandey', 28)
myList = []
myList.append(myTuple)
rameshTuple = ('Ramesh', 'Pokheral', 85)
shyamTuple = ('Shyam', 'Pandey', 33)
myList.append(shyamTuple)
myList.append(rameshTuple)
myList.sort(key=lambda x: x[0])
print(myList)
