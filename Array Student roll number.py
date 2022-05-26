t= int(input())
while t>0:
    n= int(input())
    arr= list(map(int, input().split()))
    for i in range(0,n):
        if (i % 2 == 0):
            print(arr[i], end=" ")
    print()
    t-=1