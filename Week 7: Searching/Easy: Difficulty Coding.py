def main():
    t = int(input())
    while t>0:
        n = int(input())
        arr = list(map(int, input().split()))
        flag=0
        for i in range(n):
            if arr[i]== 1:
                flag=1
                break
        if flag==1:
            print("hard")
        else:
            print("easy")
        t-=1

if __name__ == '__main__':
    main()
