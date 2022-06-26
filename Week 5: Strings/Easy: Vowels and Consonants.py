t= int(input())
while t!=0:
    str= input()
    vowels= 0
    consonant= 0
    for i in str:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A'
                or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
            vowels+=1
        else:
            consonant+=1
    print(vowels, consonant)
    t-=1
