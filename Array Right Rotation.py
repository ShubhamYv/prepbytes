def rightRotation(arr, i, j):
    while(i<j):
        temp= arr[i]
        arr[i]= arr[j]
        arr[j]= temp
        i+=1
        j-=1

def printRightRotation(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()

def main():
    n, k= map(int, input().split())
    arr= list(map(int, input().split()))
    rightRotation(arr, n-k, n-1)
    rightRotation(arr, 0, n-k-1)
    rightRotation(arr, 0, n-1)
    printRightRotation(arr, n)

if __name__ == '__main__':
    main()