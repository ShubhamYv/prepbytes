n= int(input())
arr= list(map(int,input().split()))
freq= [0]*121
for i in range(n):
    freq[arr[i]]+=1
ans=0
for i in range(1,121):
    for j in range(1,121):
        if (i<=j*0.5+7):
            continue
        if (i>100 and j<100):
            continue
        if(i>j):
            continue
        ans+= freq[i]*freq[j]
        if (i==j):
            ans-=freq[i]
print(ans)
