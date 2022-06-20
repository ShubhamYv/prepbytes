def rearrange(arr, n):
    temp = n * [None]
    small, large = 0, n - 1
    flag = True
    for i in range(n):
        if flag is True:
            temp[i] = arr[large]
            large -= 1
        else:
            temp[i] = arr[small]
            small += 1

        flag = bool(1 - flag)
    for i in range(n):
        arr[i] = temp[i]
    return arr

def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=' ')
    print()

def main():
    t= int(input())
    while t>0:
        n= int(input())
        arr= list(map(int,input().split()))
        rearrange(arr, n)
        printArray(arr,n)
        t-=1
if __name__ == "__main__":
    main()
