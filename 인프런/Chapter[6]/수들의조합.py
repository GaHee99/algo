import sys
sys.stdin = open("인프런/Chapter[6]/input.txt",'r')

n, k = map(int,input().split())
li = list(map(int,input().split()))
baesu = int(input())
res=[0]*k
count=0
def DFS(L, sum ,next):
    global count
    if L==k :
        if sum%baesu==0:
            count+=1
    else:
        for i in range(next, n):
            res[L]=li[i]
            DFS(L+1, sum+li[i], i+1)
DFS(0,0,0)
print(count)