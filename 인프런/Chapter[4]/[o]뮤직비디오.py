import sys
sys.stdin=open("인프런\Chapter[4]\input.txt", "r")
def Count(n):
    res = 0
    cnt = 1
    for i in li:
        if res+i>n:
            res=i
            cnt+=1
        else:
            res+=i
    return cnt

n , m = map(int,input().split())
li = list(map(int,input().split()))

lt = min(li)
rt = sum(li)
maxx = max(li)
res = 0 
while lt<=rt:
    mid = (lt + rt)//2
    if mid>=maxx and Count(mid)<=m:
        res=mid
        rt = mid-1
    else:
        lt = mid+1
print(res)