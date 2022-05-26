def stockMarket(prices, n):
    profit = 0
    for i in range(1, n):
        if prices[i] > prices[i - 1]:
            profit += (prices[i] - prices[i - 1])
    return profit

def main():
    t = int(input())
    while t > 0:
        n= int(input())
        arr= list(map(int, input().split()))
        print(stockMarket(arr, n))
        t -= 1
if __name__ == '__main__':
    main()