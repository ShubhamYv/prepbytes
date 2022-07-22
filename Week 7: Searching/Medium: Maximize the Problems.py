n,k= map(int, input().split())
x= 240-k
time= 0
y = 0
for i in range(1,n+1):
    if (time+5*i)<=x:
        time+=(5*i)
        y += 1
print(y)
