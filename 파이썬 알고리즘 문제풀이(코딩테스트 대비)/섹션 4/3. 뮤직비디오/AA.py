import sys
# sys.stdin=open("인프런\Chapter[4]\input.txt", "r")


N,M = map(int,input().split())
li = list(map(int,input().split()))
lt = 1
rt = sum(li)

def check(x):
    count=1
    res=0
    for i in li:
        if (res+i)<=x:
            res+=i
        else:
            res=i
            count+=1
    return count

res=0
while lt<=rt:
    middle = (lt+rt)//2
    if check(middle)>M: #더 크게 용량을 늘려야함 
        lt=middle+1
    elif check(middle)==M:
        res = middle
        rt=middle-1 
    else:
        rt= middle-1

print(res)