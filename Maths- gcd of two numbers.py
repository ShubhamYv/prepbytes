def hcf(a, b):
    if (b == 0):
        return a
    else:
        return hcf(b, a % b)


def main():
    t= int(input())
    while t>0:
        a,b= map(int, input().split())
        print(hcf(a, b))
        t-=1

if __name__ == '__main__':
    main()