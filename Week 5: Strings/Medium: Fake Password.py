t= int(input())
while t>0:
    org= input()
    fake= input()
    lf= fake[0:2]
    lr= fake[2: ]
    left= lr+lf
    right= fake[len(fake)-2: ]+ fake[0: len(fake)-2]
    if (org==left or org== right):
        print("Yes")
    else:
        print("No")
    t-=1
