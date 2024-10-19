num=input("Enter the numbers: ")
num=[float(numbers) for numbers in num.split()]
calculation='''
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulous
6. Power
7. Factorial
'''
print(calculation)
def add(num):
    res=0
    for i in num:
        res=res+i
    print(res)
def sub(num):
    res=num[0]
    for i in num[1:]:
        res=res-i
    print(res)
def mul(num):
    res=num[0]
    for i in num[1:]:
        res=res*i
    print(res)
def div(num):
    res=num[0]
    for i in num[1:]:
        if i==0:
            print("Error: can't divide by 0")
            return
        res=res/i
    print(res)
def mod(num):
    res=num[0]
    for i in num[1:]:
        if i==0:
            print("Error:modulous by o is not allowed")
            return
        res=res%i
    print(res)
mod(num)
def pow(num):
    if len(num)<2:
        print("Error: At least two numbers are required for power operation.")
        return
    base=num[0]
    exponent=num[1]
    res=base**exponent
    print("Result of power:",res)
def fact(n):
    if n<0:
        return "Error: Factorial is not defined for negative numbers."
    elif n==0:
        return 1
    else:
        return n*fact(n-1)
while True:
    option=int(input("Enter the option: "))
    if option==1:
        add(num)
    elif option==2:
        sub(num)
    elif option==3:
        mul(num)
    elif option==4:
        div(num)
    elif option==5:
        mod(num)
    elif option==6:
        pow(num)
    elif option==7:
        if len(num) != 1:
            print("Error: Factorial requires exactly one number.")
        else:
            result = fact(int(num[0]))  # Ensure to convert the first number to int
            print("Result of Factorial:", result)
    else:
        print("Enter the correct option!!")
        break