def main():
    t= int(input())
    while t>0:
        n, k= map(int, input().split())
        arr= list(map(int, input().split()))
        sum=0
        for i in range(k):
            sum+= arr[i]
        max=sum
        for j in range(k, n):
            sum= sum-arr[j-k]+arr[j]
            if sum> max:
                max=sum
        print(max)
        t-=1
if __name__ == '__main__':
    main()