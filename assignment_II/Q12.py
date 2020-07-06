# 12. Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.

def is_palindrome(str):
    palindorme = False
    for i in range(len(str)):
        if(str[i]==str[len(str)-1-i]):
            palindorme = True
        else:
            palindorme = False

    return palindorme

print(is_palindrome('RaaR'))