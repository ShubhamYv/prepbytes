s = input()
n=len(s)
a = 0
for i in range(n):
    print(s[0:a])
    a+=1
print(s)
for i in range(n-1,-1,-1):
    for j in range(i,n):
        print(s[j],end="")
    print()
