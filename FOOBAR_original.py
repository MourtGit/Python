'''Print numbers from 1 to 15 in a new line. If the number is a multiple of 3 then print FOO,
if the number is a multiple of 5 then print BAR, and if the number is a multiple of 3 and 5 
then print FOOBAR, otherwise just print the number.'''

for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print("FOOBAR")
    elif i % 3 == 0:
        print("FOO")
    elif i % 5 == 0:
        print("BAR")
    else:
        print(i)
