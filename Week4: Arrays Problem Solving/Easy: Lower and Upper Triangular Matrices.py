n,m= map(int,input().split())
m1=[]
for i in range(n):
    m1.append(list(map(int,input().split())))
#LOWER MATRIX:
for i in range(n):
    for j in range(m):
        if (i < j):
            print("0", end=" ")
        else:
            print(m1[i][j],end=" ")
    print()

#UPPER MATRIX:
for i in range(n):
    for j in range(m):
        if (i > j):
            print("0", end=" ")
        else:
            print(m1[i][j],end=" ")
    print()
