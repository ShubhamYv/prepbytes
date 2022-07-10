def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)

from sys import setrecursionlimit
setrecursionlimit(11000)

def main():
    t= int(input())
    while t!=0:
        n= int(input())
        print(fib(n))

        t-=1

if __name__== '__main__':
    main()
