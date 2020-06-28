# 13. Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).

def sortedForm(sequence):
    lst = sequence.split(',')
    lst = list(dict.fromkeys(lst))
    lst.sort()
    return (lst)

print(sortedForm('apple,is,green,is'))