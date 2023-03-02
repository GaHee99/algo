import sys
sys.stdin=open("인프런\Chapter[4]\input.txt", "r")

k,n = map(int,input().split())
li = []
for i in range(k):
    li.append(int(input()))

def Count(n):
    cnt = 0 
    for i in li:
        cnt += i//n    
    return cnt

lt = 1
rt = max(li)
res = 0 
while lt<=rt :
    mid = (lt+rt)//2
    if Count(mid) >= n:
        lt = mid +1
        res = mid
    else:
        rt = mid-1

print(res)



