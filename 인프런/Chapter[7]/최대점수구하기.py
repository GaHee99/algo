import sys
sys.stdin = open("인프런/Chapter[7]/input.txt")

n, limit = map(int,input().split())
problems = []
for i in range(n):
    score, time = map(int,input().split())
    problems.append((score,time))
Max= 0 
ch=[0]*n
def DFS (L,score, time):
    global Max
    if time>limit:
        return
    if L==n:
        if score>Max:
            Max = score 
    else:
        DFS(L+1, score+problems[L][0],time+problems[L][1])
        DFS(L+1, score,time)
DFS(0,0,0)
print(Max)
