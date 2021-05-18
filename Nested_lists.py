grades=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    students=[]
    students.append(name)
    students.append(score)
    grades.append(students)
second_highest = sorted(list(set([marks for name, marks in grades])))[1]
print(second_highest)
print("\n".join([a for a,b in sorted(grades) if b == second_highest]))