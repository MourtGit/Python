''' This program will ask a student for their grade in five subjects.
Calculates the average grade and prints grade from A to E.
A > 90
B > 80
C > 70
D > 60
E === Failed '''
subject=["Math", "Physics", "Chemistry", "Biology", "Social Study"]
grade=[]
for i in subject:
    user_grade=float(input(f"Between 0 and 100, enter your grade in {i}: "))
    if 0<= user_grade <= 100:
        grade.append(user_grade)
    else:
        print ("Enter a grade between 0 and 100")
ave_grade=sum(grade)/len(grade)
if ave_grade > 90:
    print(f"Your average grade is {ave_grade}, and your letter grade is A")
elif ave_grade > 80:
    print(f"Your average grade is {ave_grade}, and your letter grade is B")
elif ave_grade > 70:
    print(f"Your average grade is {ave_grade}, and your letter grade is C")
elif ave_grade > 60:
    print(f"Your average grade is {ave_grade}, and your letter grade is D")
else:
    print(f"Your average grade is {ave_grade}, and your letter grade is E === Failed")
    