t=int(input())
while t>0:
    n = int(input())
    a = list(map(int, input().split()))

    if a[0] > a[1]:
        print("0")

    for i in range(1, n - 1):
        if a[i] > a[i + 1] and a[i] > a[i - 1]:
            print(i)


    if a[n - 1] > a[n - 2]:
        print(n - 1)

    t-=1
