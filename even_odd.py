'''
This program takes a number between 1 and 100 and then
returns whether that number is EVEN or ODD.
'''

def even_odd(num):
    if 1<= num <= 1_00: # 1_00 or 1_000 mean 100 or 1000, separator for readability
        if num % 2 == 0:
            return f"Your number {num} is EVEN"
        else:
            return f"Your number {num} is ODD"
    else:
        return f"Number {num} is out of range. Please enter a number between 1 and 100"
    
result=even_odd(55)
print(result)



'''
This program asks the user for a number between 1 and 100 and then
checks whether that number is EVEN or ODD.
It will show: Your number user_number is even/odd.
'''

# user_input=int(input("Enter a number between 1 and 100: "))
# if 1<= user_input <= 1_00: # 1_00 or 1_000 mean 100 or 1000, separator for readability
#     if user_input % 2 == 0:
#         print(f"Your number {user_input} is EVEN")
#     else:
#         print(f"Your number {user_input} is ODD")
# else:
#     print("Please enter a number within 1 to 100")
