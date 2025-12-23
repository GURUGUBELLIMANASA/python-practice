#simple calculator program
def add(a,b);
return a+b
def subtract(a,b);
return a-b
def multiply(a,b);
return a*b
def divide(a,b);

if b==0:
return "error! division by zero:"
return a/b
print("...simple calculator...")
print("1. add ")
print("2. substraction")
print("3. multiplication")
print("4. divide")
choice = input ("enter your choice (1/2/3/4)")
num1=float(input("enter the first numner"))
num2=float(input("enter the second number"))
if choice =='1'
print("addtion=",add(num1,num2))
elif choice == '2'
print("substraction =",sub(num1,num2))
elif = choice =='3'
print("multiplication=",mul(num1,num2))
elif choice=='4'
print("division="=div(num1,num2))
else :
    print("invalid input") 
     Calculator Project (Python)

## Description
This is a simple calculator application written in Python.
It performs basic arithmetic operations such as:
- Addition
- Subtraction
- Multiplication
- Division

## How to Run
1. Install Python
2. Open terminal or command prompt
3. Run the command:
   python calculator.py

## Author
Second Year B.Tech CSE Student