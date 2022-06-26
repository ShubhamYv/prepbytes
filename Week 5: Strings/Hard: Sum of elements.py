t= int(input())
while t>0:
    n= int(input())
    arr = list(map(int,input().split()))
    sum = 0
    for i in range(0, n):
        sum = sum + arr[i]
    print(str(sum))
    t-=1
