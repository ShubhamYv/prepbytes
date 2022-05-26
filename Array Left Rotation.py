def leftRotation(arr, i, j):
    while(i<j):
        temp= arr[i]
        arr[i]= arr[j]
        arr[j]= temp
        i+=1
        j-=1

def printleftRotation(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()

def main():
    t= int(input())
    while t>0:
        n, k= map(int, input().split())
        arr= list(map(int, input().split()))
        leftRotation(arr, 0, k-1)
        leftRotation(arr, k, n-1)
        leftRotation(arr, 0, n-1)
        printleftRotation(arr, n)
        t-=1

if __name__ == '__main__':
    main()