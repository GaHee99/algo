import sys
sys.stdin = open("인프런/Chapter[6]/input.txt",'r')

#두 부분집합의 합이 서로 같으면 "YES"
n = int(input())
s = list(map(int,input().split()))
def DFS(L, Sum):
    if Sum > sum(s) - Sum:
        return 
    if L == n :
        if Sum == sum(s)-Sum:
            print("YES")
            sys.exit(0)
        else:
            return False
    else:
        DFS(L+1, Sum+s[L])
        DFS(L+1,Sum)

if(DFS(0,0)==False):
    print("NO")
