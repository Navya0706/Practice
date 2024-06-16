class Calculator:
    def _init_(self,a,b):
        self.a=a
        self.b=b
        print("am a default constructor")
    def add(a,b):
            return a+b
    def sub(a,b):
            return a-b
    def mul(a,b):
            return a*b

obj1=Calculator
print(obj1.sub(10,8))