class1=str(input("What is your 1st class"))
class2=str(input("What is your 2st class"))
class3=str(input("What is your 3rd class"))

grade1=int(input("1st grade"))
grade2=int(input("2nd grade" ))
grade3=int(input("3rd grade" ))

print("1st grade is" +str(class1))
print("2nd grade is " +str(class2))
print("3rd grade is " +str(class3))

if grade1>=90:
    print('A')
elif grade1>=80:
    print('B')
elif grade1>=70:
    print('C')
elif grade1>=60:
    print('D')
else:
    print('F')

if grade2>=90:
    print('A')
elif grade2>=80:
    print('B')
elif grade2>=70:
    print('C')
elif grade2>=60:
    print('D')
else:
    print('F')

if grade3>=90:
    print('A')
elif grade3>=80:
    print('B')
elif grade3>=70:
    print('C')
elif grade3>=60:
    print('D')
else:
    print('F')


average=(float((grade1+grade2+grade3)/3))
print("The average is: ", average)
#assume all have 4 credits
gpa=(float((grade1+grade2+grade3)/300)*4)
print("The GPA is: ", gpa)
