t= int(input())
while t>0:
    num= int(input())
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                print("No")
                break
        else:
            print("Yes")
    else:
        print("No")
    t-=1