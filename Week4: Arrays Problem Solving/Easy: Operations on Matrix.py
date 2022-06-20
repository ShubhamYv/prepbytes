n,m= map(int,input().split())
m1=[]
for i in range(n):
    m1.append(list(map(int,input().split())))

m2=[]
for i in range(n):
    m2.append(list(map(int,input().split())))

m3=[]
for i in range(n):
    m3.append([0]*m)
#ADDITION:
for i in range(n):
    for j in range(m):
        m3[i][j] = m1[i][j] +m2[i][j]

for i in range(n):
    for j in range(m):
        print(m3[i][j], end=' ')
    print()
#MULTIPLICATION:

m3=[]
for i in range(n):
    m3.append([0]*m)

for i in range(n):
    for j in range(m):
        for k in range(m):
            m3[i][j]= m3[i][j]+ (m1[i][k]*m2[k][j])

for i in range(n):
    for j in range(m):
        print(m3[i][j], end=' ')
    print()
