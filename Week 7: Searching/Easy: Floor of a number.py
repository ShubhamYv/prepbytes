def floor(arr, n, ele):
    low = 0
    high = n-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == ele:
            return mid
        if mid==low:
            return mid
        if arr[mid] >= ele:
            high = mid
        else:
            low = mid
    return low


t = int(input())
while t > 0:
    n, ele = map(int, input().split())
    arr = list(map(int, input().split()))
    flag=0
    if ele>=arr[0] and ele<arr[n-1]:
        print(floor(arr, n, ele))
    if ele>= arr[n-1] :
        print(n-1)
    if ele<arr[0]:
        print("-1")
    t-=1
