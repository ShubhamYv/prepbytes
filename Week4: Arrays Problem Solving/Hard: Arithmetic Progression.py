def main():
    t=1
    while(t!=0):
        n = int(input())
        arr = list(map(int, input().split()))
        visitCount = [0]*100001
        prevIndex = [0]*100001
        diff = [0]*100001
        for i in range(n):
            if(visitCount[arr[i]]==-2):
                continue
            visitCount[arr[i]]+=1
            if(visitCount[arr[i]]==2):
                diff[arr[i]] = i - prevIndex[arr[i]]
            elif (visitCount[arr[i]]>2):
                if(i - prevIndex[arr[i]]!=diff[arr[i]]):
                    visitCount[arr[i]]=-2
                    continue  
            prevIndex[arr[i]]=i
        count=0
        for i in range(len(visitCount)):
            if(visitCount[i]>0):
                count+=1
        print(count)
        for i in range(len(visitCount)):
            if(visitCount[i]>0):
                print(i,diff[i])
        t=t-1
if __name__ == '__main__':
    main()
