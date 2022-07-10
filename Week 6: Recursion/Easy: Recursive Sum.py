def sumOfN(n):
    if n==0:
        return  0
    return n+ sumOfN(n-1)

from sys import  setrecursionlimit
setrecursionlimit(11000)

def main():
    t= int(input())
    while t!=0:
        n= int(input())
        print(sumOfN(n))
        t-=1
if __name__ == "__main__":
    main()
