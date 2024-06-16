class Calculator:
    def add(self,*args):
        sum = 0
        for num in args:
            sum=sum+num
        return sum
calculator=Calculator()
print(calculator.add(1,2))
print(calculator.add(1,2,3,))
print(calculator.add(1,2,3,4))