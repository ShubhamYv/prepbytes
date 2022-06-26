t= int(input())
while t>0:
    n= int(input())
    str= input()
    for i in range(len(str)):
        a=str.count("A")
        d=str.count("D")
        if a>d:
            print("Aditya")
            break
        elif d>a:
            print("Danish")
            break
        else:
            print("AdiDan")
            break
    t-=1
