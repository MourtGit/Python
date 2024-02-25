'''
This program asks the user for a number between 1 and 100 and then
checks whether that number is EVEN or ODD.
It will show: Your number user_number is even/odd.
'''

user_input=int(input("Enter a number between 1 and 100: "))
if 1<= user_input <= 100:
    if user_input % 2 == 0:
        print(f"Your number {user_input} is EVEN")
    else:
        print(f"Your number {user_input} is ODD")
else:
    print("Please enter a number within 1 to 1000")