"""nums=[]
ans=int(input("How many students are in the class?"))

while ans>0:
    nums.append[ans,ans-1]
    if ans=0
        continue"""
import array as arr
# Student name and Student grade then repeat until everyone's grade has been entered
students = []
grades = []
while True:
    name = input("Enter student's name: ")
    grade = input(f"Enter {name}'s grade: ")
    grades.append(int(grade))
    repeat = input("Do you want to enter another student? ")
    students.append([name, grade])
    if repeat.lower() == "yes":
        continue
    else:
        break

# print everyone's name and grade
print(students)

# Calculate class average
x = len(grades)
y = sum(grades)
avg_grade = y/x
print("Average Class Grade:", avg_grade)
