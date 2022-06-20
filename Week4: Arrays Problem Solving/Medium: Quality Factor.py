try:
    n = int(input())
    B = list(map(int, input().split()))
    orp = abs(B[0])
    for i in range(1, n):
        orp = orp + abs(B[i] - B[i - 1])
    print(orp)
except:
    pass
