t = int(input())

while t>0:
    n =  int(input())
    arr = list(map(int,input().split()))
    
    aipi = []
    aimi = []
    for i in range(n):
        aipi.append(arr[i]+i)
    
    for i in range(n):
        aimi.append(arr[i]-i)
        
    v1 = max(aipi) - min(aipi)
    v2 = max(aimi) - min(aimi)
