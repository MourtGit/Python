'''This program prints digits of a number in reverse order on the same line.
If the number has only one digit, print that digit.
Leverage %10
''' 

num=int(input("Enter a number: "))
reverse=0
sign=1
if num < 0:
    sign=-1
    num*=-1
while num > 0:
    modulo=num % 10
    reverse=reverse * 10 + modulo
    num //= 10
print(reverse*sign)