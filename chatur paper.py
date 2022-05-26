arr= list(map(str, input().split()))
a,b,c,d=1,2,3,4
count=0
for i in range(len(arr)):
    if arr[len(arr)-1]==c:
        count=b
    if arr[len(arr)-1]==d or arr[len(arr)-2]== c:
        count=d
    if arr[i]== arr.reverse():
        count=0
    print(count)