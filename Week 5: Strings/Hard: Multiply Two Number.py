t= int(input())
while t>0:
    arr = list(map(int,input().split()))
    mul = 1
    for i in range(0, len(arr)):
        mul = mul*arr[i]
    print(str(mul))
    t-=1
