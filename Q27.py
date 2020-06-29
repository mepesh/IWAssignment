# 27. Write a Python program to replace the last element in a list with another list

def replaceLastItem(lst,repLst):
    returnList = []
    returnList = lst[0:-1]
    for i in range(len(repLst)):
        returnList.append(repLst[i])

    return(returnList)
print('The last item in list 1 has been replaced ',replaceLastItem([1,2,3,4],[11,12,13]))