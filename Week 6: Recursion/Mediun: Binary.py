def binary(n, prev, output, i):
    if n==0:
        for j in range(len(output)):
            print(output[j], end="")
        print()
        return
    if prev==0 or prev==-1:
        output[i]=0
        binary(n-1,0,output,i+1)
        output[i]=1
        binary(n-1,1,output,i+1)

    else:
        output[i]=0
        binary(n-1,0,output,i+1)

def main():
    t= int(input())
    while t>0:
        n= int(input())
        output= [-1]*n
        binary(n,-1,output,0)
        t-=1

if __name__=='__main__':
    main()
