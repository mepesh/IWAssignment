# 7. Create a list of tuples of first name, last name, and age for your
# friends and colleagues. If you don't know the age, put in None.
# Calculate the average age, skipping over any None values. Print out
# each name, followed by old or young if they are above or below the
# average age.

person1 = ('Dipesh','Pandey',28)
person2 = ('Ramesh','Pokheral', 35)
person3 = ('Bipana','Pokheral', 32)

listPerson = [person1,person2,person3]
ageTotal = 0
for i in range(len(listPerson)):
    data = listPerson[i]
    if(type(data[2]) is int):
        ageTotal+=data[2]

averageAge = int(ageTotal/3)
print(averageAge)

for i in range(len(listPerson)):
    data = listPerson[i]
    if(data[2]>averageAge):
        print(f' {data[0]}  {data[1] } old')
    else:
        print(f' {data[0]}  {data[1] } young')




