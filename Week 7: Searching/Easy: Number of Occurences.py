def main():
    t = int(input())
    while t>0:
        n = int(input())
        arr = list(input().split())
        res=0
        for i in range(n+1):
            res= arr.count('x')
        print(res)
        t-=1

if __name__ == '__main__':
    main()
