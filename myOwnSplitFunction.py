def mysplit(strng):
    #
    i=0
    strng=strng.strip(" ")

    cnt=strng.find(" ")
    ls=[]
    if(strng.isspace()or len(strng)==0):
        return ls 
    if(cnt==-1):
        ls.append(strng)
        return ls
    ls.append(strng[:cnt])
    while cnt!=-1:
        prev=cnt+1
        cnt=strng.find(" ",prev)

        if(cnt!=-1):
            ls.append(strng[prev:cnt])
        else:
            ls.append(strng[prev::])

    return ls



print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
