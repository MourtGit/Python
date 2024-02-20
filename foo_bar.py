# FooBar

num = int(input("Enter a number between 0 and 50: "))
if not 0 <= num <= 50:
    print("Please enter a number between 0 and 50.")

elif num % 5 == 0 and num % 7 == 0:
        print ("FooBar")
elif num % 5 == 0:
        print("Foo")
elif num % 7 == 0:
        print("Bar")
else:
    print (num)
