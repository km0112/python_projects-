"""Project Details - Updating our Grading program
Must use a minimum of three functions in this program (how you integrate/use/place the functions is up to you)
Start with:
Ask the user (teacher in this case) to enter a student name (as many as the teacher has)
Collect up to 3 test grades for each student (you can do this when you take in the student's name or

after you collect the names and use the student name as a prompt to ask for their grades)
Once you have collected the names and grade do the following in any order

print the average for each student (is saving this data to a parallel array useful?)

print the average for each test ([r][1], notice i locked the column here)

print each student's name with each test grade and that student's average for all three tests"""

c=[]
g=[]
tests=["test1","test2","test3"]
testaverage1=[]
testaverage2=[]
testaverage3=[]

def get_grades():
    rep=int(input("how many students do you want to enter?"))
    while rep>0:
        name=input("What is the student's name?")
        c.append(name)
        ans = int(input("What grade did your student get on test one?"))
        g.append(ans)
        ans2 = int(input("What grade did your student get on test 2?"))
        g.append(ans2)
        ans3 = int(input("What grade did your student get on test 3?"))
        g.append(ans3)
        rep=rep-1

get_grades()

def get_student():
    s=input("What student do you want test grades for?")
    if s in c:

        print(c.index(s))
        f=int(3*(c.index(s)))
        print(g[f], g[f+1], g[f+2])
get_student()

def get_average():
    test=input("What test do you want grades for?")
    a=tests.index("test1")
    b=tests.index("test2")
    d=tests.index("test3")

    if "test1" in test:
        for student in c:
            f=int(3*(c.index(student)))
            print(g[f])
            testaverage1.append(g[f])

    if "test2" in test:
        for student in c:
            f=int(3*(c.index(student)))
            print(g[f+1])
            testaverage2.append(g[f+1])

    if "test3" in test:
        for student in c:
            f=int(3*(c.index(student)))
            print(g[f+2])
            testaverage3.append(g[f+2])

    if "test1" in test:
        print("The average of test 1 is", sum(testaverage1)/len(testaverage1))
    if "test2" in test:
        print("The average of test 2 is", sum(testaverage2)/len(testaverage2))
    if "test3" in test:
        print("The average of test 3 is", sum(testaverage3)/len(testaverage3))

get_average()

classavg= print((sum(g))/len(g))
