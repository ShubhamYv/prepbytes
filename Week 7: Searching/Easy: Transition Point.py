def indexOfFirstOne(arr, n):
    for i in range(0, n):
        if (arr[i] == 1):
            return i
    return -1

def main():
    t= int(input())
    while t>0:
        n= int(input())
        arr= list(map(int,input().split()))
        ans = indexOfFirstOne(arr, n)
        print(ans)
        t-=1

if __name__ == '__main__':
    main()
