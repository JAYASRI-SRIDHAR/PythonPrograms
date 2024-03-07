ls=[]
mydict={}
String=input("Input your string")
for i in range(len(String)):
  if String[i] in mydict:
    continue
  ls=[i]
  count=1
  for j in range(i+1,len(String)):
    if(String[i]==String[j]):
      ls.append(j)
      count+=1
  mydict[String[i]]=(count,ls)
print(mydict)
