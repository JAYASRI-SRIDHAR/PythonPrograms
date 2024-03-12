# Method overloading not supported by python
class Methovr():
    def func1(self, a:int)->int:
        return a*a
    def func1(self, l:int, b:int)->int:
        return l*b
obj= Methovr()
print(obj.func1(2,3))
print(obj.func1(2)) # will throw error
