import sys
# sys.stdin=open("인프런\Chapter[4]\input.txt", "r")

n,m = map(int,input().split())
li = [] 
for i in range(n):
    li.append(int(input()))
        
li.sort()
def Count(n):
    tmp = li[0]
    cnt=1
    for i in range(1,len(li)):
        distance = li[i]-tmp
        if distance>=n:
            tmp = li[i]
            cnt+=1
    return cnt
        
        

lt = li[0]
rt = li[-1]
res=0
while lt<=rt:
    mid = (lt+rt)//2
    if Count(mid)>=m:
        lt = mid + 1
        res= mid
    else:
        rt = mid -1
print(res)