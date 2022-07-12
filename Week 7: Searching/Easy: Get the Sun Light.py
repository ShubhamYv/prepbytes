t=int(input())
while t>0:
    n=int(input())
    arr=list(map(int,input().split()))
    count=1;
    val=arr[0]
    for i in range(1,n):
        if(arr[i]>val):
            count+=1
            val=arr[i]
    t-=1
    print(count)
