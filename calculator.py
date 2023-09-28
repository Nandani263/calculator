def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def power(a):
    return a*a




print("select operation")
print("1.ADD")
print("2.SUBTRACTION")
print("3.MULTIPLY")
print("4.DIVIDE")
print("5.square")
while True:
    choice =input("Enter choice-1/2/3/4/5 ")
    if choice in('1','2','3','4','5'):
        a =float(input("Enter the first number:"))
        b =float(input("enter the second number:"))

        if choice =='1':
            print(a,"+",b,"=",add(a,b))
        elif choice =='2':
            print(a,"-",b,"=",subtract(a,b))
        elif choice =='3':
            print(a,"*",b,"=",multiply(a,b))
        elif choice =='4':
            print(a,"/",b,"=",divide(a,b))
        elif choice =="5":
            print(a,"^",a,"=",power(a))
            next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            
           
        
            break
        else:
            print("next")






