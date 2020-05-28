if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    a=student_marks[query_name]
    b=0
    for i in range(0,3):
        b=b+a[i]

    c=b/3
    #float(c)
    print("{:.2f}".format(c))
        
