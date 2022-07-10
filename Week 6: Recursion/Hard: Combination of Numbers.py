def combi(arr, op, i, index, n, k):
    if k==0:
        for j in range(len(op)):
            print(op[j], end=" ")
        print()
        return
    for j in range(i, n):
        op[index]= arr[j]
        combi(arr, op, j+1, index+1, n, k-1)


def main():
    n= int(input())
    arr= list(map(int, input().split()))
    k= int(input())
    op= [0]*k
    combi(arr, op, 0, 0, n, k)

if __name__ == '__main__':
    main()
