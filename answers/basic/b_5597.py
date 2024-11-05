import sys

studentCount = 30
submittedStudentNumbers = [int(sys.stdin.readline()) for _ in range(studentCount - 2)]

for i in range(1, studentCount + 1):
    if i not in submittedStudentNumbers:
        print(i)
