ls = [4, 6, 2, 7, 8, 1]
i = 0

def sortme(ls,i):
    if(ls[i]>ls[i+1]):
        ls[i],ls[i+1]=ls[i+1],ls[i]
        i=0
        sortme(ls,i)
    else:
        i+=1
        if(i<len(ls)-1):
            sortme(ls,i)
    return ls
print(sortme(ls,i))
