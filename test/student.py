studentCount = int(input("Enter total number of students: "))

students = []
for i in range(studentCount):
    students.append(input(f"Enter name of student {i+1}: "))
print("\nStudent Details:")

for i in range(len(students)):
    print(f"student {i + 1} is = {students[i]}")