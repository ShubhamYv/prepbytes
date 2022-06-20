def arrayrotation(arr, i, j):
    while (i<j):
        temp= arr[i]
        arr[i]= arr[j]
        arr[j]= temp
        i+=1
        j-=1
def printarray(arr,n):
    for i in range(n):
        print(arr[i], end=' ')
    print()
def main():
    t= int(input())
    while t>0:
        n,k= map(int,input().split())
        arr= list(map(int,input().split()))
        k=k%n
        arrayrotation(arr, n-k, n-1)
        arrayrotation(arr, 0, n-k-1)
        arrayrotation(arr, 0, n-1)
        printarray(arr,n)
        t=t-1
        
if __name__ == "__main__":
    main()
