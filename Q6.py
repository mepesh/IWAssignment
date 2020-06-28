#6. Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.

sampleSentence = 'Python is poor and not bad and is for people '
notIndex = sampleSentence.find('not')
print(notIndex)
poorIndex = sampleSentence.find('poor')
print(poorIndex)

if(poorIndex>notIndex & poorIndex!=-1):
    returnString = sampleSentence[0:poorIndex] + 'good'

else:
    returnString = sampleSentence

print(returnString)


