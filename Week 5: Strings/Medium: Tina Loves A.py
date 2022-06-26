t= int(input())
while (t!=0):
    str= input()
    A=0
    res=0
    for i in range(len(str)):
        if str[i]== 'a':
            A+=1
            res= min(2 * A - 1, int(len(str)))
    print(res)

    t-=1
