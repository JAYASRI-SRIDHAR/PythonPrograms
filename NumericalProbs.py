def OneToNPrime(N):
  for n in range(2,N):
      for i in range(2,n):
            if(n%i==0):
                      break
      else:
            print(n)

        
def RevNum(N):
    length=len(str(N))
    a=N
    sum1=0
    rev=0
    for i in range(length):
        a=N%10
        N=N//10
        sum1=sum1*10+a
    return sum1
                
def FindFact(N,a=1,count=1):
        if (N==0 or N==1):
            return 1
        if N>2:
            a=a*(count)
            
            if(count==N):
                print(a)
            else:
                count+=1
                FindFact(N,a,count)
class NumbChallenges:
    
    def FindMyAvg(self,count):
        self.count=count
        x=0
        y=0
        for i in range(count):
            x=int(input("Enter the list items: "))
            y=y+x
        print("average= ",y/self.count)

                        
def Primeornot(n):
    for i in range(2,round(n/2)+1):
        if(n%i==0):
            return "Not Prime"
    else:
        return "Prime"
inp=input("What do you want to do now?  onetoprime? prime? avg? rev? fact?")


if(inp=="avg"):
    count=int(input("Enter the count of the list: "))
    NumbObj=NumbChallenges()
    NumbObj.FindMyAvg(count)
elif(inp=="onetoprime"):
    N=int(input("Enter N: "))
    OneToNPrime(N)
elif(inp=="prime"):
    N=int(input("Enter N: "))
    print(Primeornot(N))
elif(inp=="rev"):
    N=int(input("Enter N: "))
    print(RevNum(N))
elif(inp=="fact"):
    N=int(input("Enter N: "))

    FindFact(N)

