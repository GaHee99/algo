import sys
sys.stdin = open("인프런/Chapter[6]/input.txt",'r')


n,Sum = map(int,input().split())

numbers = [0]*n
ch=[0]*(n+1)
mul = [1]*n
res= 0 
def DFS(L):
    global count
    global res 
    if L == n:
        for k in range(n):
            res += numbers[k]*mul[k]
        if res == Sum:
            for i in numbers:
                print(i,end=' ')
            sys.exit(0)
        else:
            res=0
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                numbers[L]=i
                ch[i]=1
                DFS(L+1)
                ch[i]=0
def multiple(n):
    for i in range(1,n):
        mul[i]= mul[i-1]*(n+1-i)//(i)
multiple(n-1)
DFS(0)