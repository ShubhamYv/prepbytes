def main():
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    freq = [0] * 100001
    for i in range(n):
        freq[arr[i]] += 1
    for i in range(100001):
        if freq[i] == k:
            print(i)
            break

if __name__ == '__main__':
    main()
