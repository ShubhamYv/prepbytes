t= int(input())
while t>0:
    s= input()
    max_char= 26
    char_count=[0]*26
    for i in range(0, len(s)):
        char_count[ord(s[i]) - ord('a')] += 1
    for i in range(max_char - 1, -1, -1):
        for j in range(char_count[i]):
            print(chr(97 + i), end="")
    print()
    t-=1
