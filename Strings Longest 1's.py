n, k= map(int,input().split())
arr= list(map(int, input().split()))
count=0
for i in range(n):
    if arr[i]==1:
        count+=1
print(count)