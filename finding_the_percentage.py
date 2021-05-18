if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for x,y in student_marks.items():
        if x == query_name:
            total = sum(student_marks[query_name])/3
            print(f"{total:.2f}")
            break
            