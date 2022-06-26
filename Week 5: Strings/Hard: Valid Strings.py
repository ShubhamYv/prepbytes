def validString(s, n):
    if n % 2 == 1:
        return False
    k = "("
    k = k + s + ")"
    d = []
    count = 0
    for i in range(len(k)):
        if k[i] == "(":
            d.append("(")
        else:
            if len(d) != 0:
                d.pop()
            else:
                return False
    if len(d) == 0:
        return True
    return False

def main():
    t= int(input())
    while t>0:
        S = input()
        n = len(S)
        if (validString(S, n)):
            print("Yes")
        else:
            print("No")
        t-=1

if __name__ == '__main__':
    main()
