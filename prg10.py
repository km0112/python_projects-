courses= int(input("How many grades are you averaging?"))
x=0
track = 0
while x<courses:
    x=x+1
    subject=str(input("What is the subject?"))
    grade=int(input("What grade did you get?"))
    print(subject)
    if grade>=90:
        print('You got an A for',subject)
    elif grade>=80:
        print('You got a B for',subject)
    elif grade>=70:
        print('You got a C for',subject)
    elif grade>=60:
        print('You got a D for',subject)
    else:
        print('You got an F')
    track = track + grade
avg = track/courses
if avg>=90:
    print('Your class average ia an A')
elif avg>=80:
    print('Your class average ia a B')
elif avg>=70:
    print('Your class average ia a C')
elif avg>=60:
    print('Your class average ia a D')
else:
    print('Your class average ia an F')
