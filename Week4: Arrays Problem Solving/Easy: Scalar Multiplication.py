n,m,k = map(int,input().split())
m1=[]
for i in range(n):
    m1.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        m1[i][j]= m1[i][j]*k

for i in range(n):
    for j in range(m):
        print(m1[i][j], end=' ')
    print()
