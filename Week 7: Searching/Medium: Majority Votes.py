def main():
    t= int(input())
    while t>0:
        n= int(input())
        arr= list(map(int, input().split()))
        k= n//2
        flag=0
        freq= [0]*1000001
        for i in range(n):
            freq[arr[i]] += 1
        for i in range(1000001):
            if freq[i]>k:
                print(i)
                flag= 1
        if flag==0:
            print('-1')
        t-=1

if __name__ == '__main__':
    main()
