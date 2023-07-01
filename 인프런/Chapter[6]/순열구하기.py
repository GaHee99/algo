import sys
# sys.stdin = open("인프런/Chapter[6]/input.txt",'r')

n, m = map(int,input().split())
res = [0]* m 
ch= [0]*(n+1)
count=0
def DFS(L):
    global count
    if L==m:
        for i in res:
            print(i,end=' ')
        count+=1
        print()
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1)
                ch[i]=0


DFS(0)
print(count)