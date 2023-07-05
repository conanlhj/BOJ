n=int(input())

while(n>0):
    sum=0
    cnt=0
    score=list(map(int,input().split()))
    for i in range(len(score)):
        if i != 0:
            sum+=score[i]
    for i in range(len(score)):
        if(i != 0):
            if(sum/(len(score)-1)<score[i]):
                cnt+=1
    print("{0:0.3f}%".format(cnt/(len(score)-1)*100))
    n-=1
