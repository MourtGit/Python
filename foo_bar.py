# FooBar

num = int(input("Enter a number between 0 and 50: "))
if 0 <= num <= 50:
        if num % 5 == 0 and num % 7 == 0:
                print ("FooBar")
        elif num % 5 == 0:
                print("Foo")
        elif num % 7 == 0:
                print("Bar")
        else:
                print (num)
else:
        print("Invalid! Please enter a number between 0 and 50.")
