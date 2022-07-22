n,k=map(int,input().split())
a=list(map(int,input().split()))
count=0
bookleft=n

for i in range(n):
    if a[i]<=k:
        count+=1
        a[i]=0
    else:
        break

for i in range(n-1,-1,-1):
    if a[i]<=k and a[i]!=0:
        count+=1
    else:
        break
      
bookleft=bookleft-count

print(bookleft)
