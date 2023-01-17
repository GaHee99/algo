import sys
sys.stdin = open("인프런/Chapter[6]/input.txt",'r')

n = int(input())
numbers = list(map(int,input().split()))
total = sum(numbers)
def DFS(L,Sum):
    if Sum > total - Sum:
        return
    if L==n:
        if Sum == total - Sum:
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, Sum+numbers[L])
        DFS(L+1, Sum)

         
DFS(0,0)
print("NO")