def leastLexiString(s):
    if (len(s)==1 or len(s)==0):
        return s
    x = leastLexiString(s[0:int(len(s) / 2)])
    y = leastLexiString(s[int(len(s) / 2):len(s)])
    return min(x + y, y + x)

def areEquivalent(a, b):
    return (leastLexiString(a) == leastLexiString(b))

def main():
    a = input()
    b = input()
    if (areEquivalent(a, b)):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
