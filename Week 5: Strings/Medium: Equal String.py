t = int(input())
while t > 0:
    str = []
    x = []
    min = 1001
    county = 0
    n = int(input())
    while n > 0:
        m = input()
        str.append(m)
        n -= 1
    for i in str:
        x.append(i+i)
    for i in str:
        count = 0
        for j in x:
            if i not in j:
                min = -1
            if min != -1:
                count += j.find(i)
        if min > count:
            min = count
    print(min)
    t-=1
