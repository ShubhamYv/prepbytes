def sameStr(str):
    if str== str[::-1]:
        return "Yes"
    return "No"

def main():
    t= int(input())
    while t!=0:
        str= input()
        print(sameStr(str))
        t-=1

if __name__== '__main__':
    main()
