# 11. Write a Python program to count the occurrences of each word in a given
# sentence.

def wordCount(sentence):
    list = sentence.split()
    countDict = {}

    for i in range(len(list)):
        if list[i] in countDict:
            countDict[list[i]] += 1

        else:
            countDict[list[i]] = 1

    print(countDict)


print(wordCount('this is this beautiful house is clean'))
