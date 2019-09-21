n = int(input())
student_marks = {}

# Taking the student data from STDIN
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()

# Computing the required average
average_marks = sum(student_marks[query_name])/3
print('%.2f' %average_marks)
