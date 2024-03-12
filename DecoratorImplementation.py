#Decorator
def check(func):
    def zeroer(a, b):
        if b==0:
            return "Can't devide by 0"
        func(a, b)
    return zeroer

@check
def div(a, b):
    print(a//b)

x=int(input("Input number1"))
y=int(input("Input number2"))
if div(x,y)==None:
    pass
else:
    print(div(x,y))
