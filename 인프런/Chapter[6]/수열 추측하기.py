import sys
sys.stdin = open("인프런/Chapter[6]/input.txt",'r')


n,Sum = map(int,input().split())

numbers = [0]*n
ch=[0]*(n+1)
mul = [1]*n
for i in range(1,n):
    mul[i]= mul[i-1]*(n-i)//(i)
res= 0 
def DFS(L, sum):
    if L == n and sum == Sum:
        for x in numbers:
            print(x, end =' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                numbers[L]=i
                DFS(L+1, sum+(numbers[L]*mul[L]))
                ch[i]=0

DFS(0,0)