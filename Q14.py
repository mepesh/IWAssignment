# 14. Write a Python function to create the HTML string with tags around the word(s).

def stringToHtml(tag, string):
    # htmlString = '<tag>'+string+'</tag>'
    return f"<{tag}>{string}</{tag}>"

print('h1','IW')
