import sys
# sys.stdin=open("인프런\Chapter[4]\input.txt", "r")

n = int(input())
li = []
for i in range(n):
    start,end = map(int,input().split())
    li.append((start,end))
M = 0 
for i in range(n):
    cnt = 1
    tmpstart, tmpend = li[i]
    for k in range(i,n):
        start,end = li[k]
        if start>=tmpend:
            cnt+=1
            tmpstart=start
            tmpend=end
    M = max(M,cnt)
print(M)
     