t = int(input())
vow = 'aeiou'
while t > 0:
    flag = True
    str = input()
    for i in range(len(str) - 1):
        if str[i] not in vow and str[i] != 'n':
            if str[i + 1] not in vow:
                flag = False
    if str[len(str) - 1] not in vow and str[len(str) - 1] != 'n':
        flag = False
    if flag == False:
        print('NO')
