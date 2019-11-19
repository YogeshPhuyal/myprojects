

def add(num1, num2,num3):
    return num1 + num2+num3

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


print("Please select operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take input from the user
choice = input("Select operations form 1, 2, 3, 4 :")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("enter third number:"))
if choice == '1':
    print(num1, "+", num2,"+ ",num3,"=",
    add(num1, num2,num3))

elif choice == '2':
    print(num1, "-", num2, "=",
          subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=",
          multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=",
          divide(num1, num2))
else:
    print("Invalid input")

