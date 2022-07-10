def sum(n):
    if n==0:
        return n
    else:
        return n%10 + sum(n//10)
def main():
    t= int(input())
    while t!=0:
        n= int(input())
        print(sum(n))
        t-=1

if __name__== '__main__':
    main()
