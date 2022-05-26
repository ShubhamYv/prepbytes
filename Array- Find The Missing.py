# t= int(input())
# while t>0:
#     n= int(input())
#     arr= list(map(int, input().split()))
#     arr.sort()
#     for i in range(n-1):
#         if abs(arr[i]-arr[i+1])== 1:
#             continue
#         else:
#             print(arr[i]+1)
#     t-=1

t= int(input())
while t>0:
    n= int(input())
    arr= list(map(int, input().split()))
    arr.sort()
    m= n+1
    sum= m*(m+1)//2
    res= sum- 