class Cal:
    def __init__(self,num1=0,num2=0):
        self.num1=num1
        self.num2=num2
    def add(self):
     return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def division(self):
        return self.num1/self.num2
    def mul(self):
        return self.num1*self.num2
print('''---CALCULATOR--- 
1.ADD
2.SUBTRACT
3.MULTIPLY
4.DIVISION
Press 5 to exit''')
while True:
    option=int(input("Choose an option:"))
    if option==5:
        print('Successfully exit')
        break
    num1=float(input("Enter 1st number:"))
    num2=float(input("Enter 2nd number:"))
    op=Cal(num1,num2)
    if option==1:
        print(num1,"+",num2,"=",op.add())
    elif option==2:
       print(num1,"-",num2,"=",op.sub())
    elif option==3:
        print(num1,"×",num2,"=",op.mul())  
    elif option==4:
        print(num1,"÷",num2,"=",op.division())
