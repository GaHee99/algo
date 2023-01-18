import sys
sys.stdin = open("인프런/Chapter[6]/input.txt",'r')

n,m = map(int,input().split())
res = [0] * m
count=0
def DFS(L,t):
    global res
    global count
    if L== m :
        for i in res :
            print(i, end=' ')
        count+=1
        print()
    else:
        for k in range(t,n+1):
            res[L]=k
            DFS(L+1, k+1)
DFS(0,1)
print(count)
