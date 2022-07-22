t=int(input())
while t>0:
  n=int(input())
  a=list(map(int,input().split()))
  
  fa=abs(a[0]-a[1])
  la=abs(a[n-1]-a[n-2])
  
  k=min(fa,la)
  
  for i in range(n-1):
      if a[i]+k!=a[i+1]:
          print(a[i]+k)
          break
  t-=1
