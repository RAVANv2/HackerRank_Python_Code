#20/03/2020

#I found some error in by simply doing with list so i prefer to work with dictionary
#I can store name as index and marks as value in the form of list in dictionary

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
ans = input()
for i in student_marks:
    if ans == i:
        avg = (student_marks[ans][0] + student_marks[ans][1] + student_marks[ans][2])/3
print("{:.2f}".format(avg))
