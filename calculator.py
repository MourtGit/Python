# This program will ask for two numbers (integer or float) and calculates the sum of those two numbers.

# number1 = float(input("Enter the first number: "))
# number2=  float(input("Enter the second number: "))
# sum = number1+number2
# print (f"The sum of {number1} and {number2} is: {sum}")

import math

def cal(num1, num2, operator):
    if operator == "+":
        result = num1+num2
    elif operator == "sqrt":
        result == (num2)
    elif operator == "-":
        result = num1-num2
    elif operator == "*" or operator == "x":
        result = num1*num2
    elif operator == "/" or operator == "÷":
        if num2 !=0:
            result = num1 / num2
        else:
            result = "Division by zero is not allowed."
    elif operator == "**":
        result = num1**num2
    return result

# result=cal(6,3,"/")    # 2.0
# result=cal(6,0,"/")    # Division by zero is not allowed.
result=cal(2,3,"**")    # 6.0
print(result)