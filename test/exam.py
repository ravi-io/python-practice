total_grandMarks = 0

def exam(sem,totalSubjects):
  print(f"Semester: {sem}")
  subjectsMarks =[]
  
  for i in range(totalSubjects):
    mark = float(input(f"Enter marks for subject in sem-{i+1}: "))
    subjectsMarks.append(mark)
  print(f"Marks for semester {sem} are: {subjectsMarks}")
  global total_grandMarks
  total_grandMarks += sum(subjectsMarks)
  overallPercentage = (total_grandMarks / (totalSubjects * totalSemester)) * 100
  print(f"Overall Percentage after semester {sem}: {overallPercentage:.2f}%\n")

totalSemester = int(input("Enter semester: "))
totalSubjects = int(input("Enter total number of subjects: "))

for i in range(totalSemester):
  exam(i + 1, totalSubjects)

print(f"Grand Total Marks: {total_grandMarks}")

