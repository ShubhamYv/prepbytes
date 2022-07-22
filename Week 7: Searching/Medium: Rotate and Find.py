def main():
    t= int(input())
    while t>0:
        n= int(input())
        arr= list(map(int, input().split()))
        x= int(input())
        flag=0
        for i in range(n):
            if arr[i]==x:
                flag=1
                break
        if flag==1:
            print(i)
        else:
            print("-1")
        t-=1
        
if __name__ == '__main__':
    main()
