def printPattern(n):
    if (n == 0 or n < 0):
        print(n, end=" ")
        return
    # First print decreasing order
    print(n, end=" ")
    printPattern(n - 5)
    # Then print increasing order
    print(n, end=" ")
    return

def main():
    t = int(input())
    while t > 0:
        n = int(input())
        printPattern(n)
        print()
        t -= 1

if __name__ == '__main__':
    main()
