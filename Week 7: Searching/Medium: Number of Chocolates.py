def UpperBound(arr, n, ele):
    low=0
    high= n
    while (low<high):
        mid= (low+high)//2
        if(ele>= arr[mid]):
            low= mid+1
        else:
            high=mid
    return low

def main():
    n= int(input())
    arr1= list(map(int,input().split()))
    arr= arr1.sort()
    q= int(input())
    while q > 0:
        x= int(input())
        res= UpperBound(arr1, n, x)
        print(res)
        q-=1

if __name__ == '__main__':
    main()
