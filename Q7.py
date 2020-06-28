# 7.Write a Python function that takes a list of words and returns the length of the
# longest one.

def longestWord(words):
    longestWordCount = 0
    for i in range(len(words)):
        wordCount = len(words[i])
        if(wordCount > longestWordCount):
            longestWordCount = wordCount

    return longestWordCount


a = longestWord(['Apple', 'Thisisamazing', 'wassup'])
print(a)
