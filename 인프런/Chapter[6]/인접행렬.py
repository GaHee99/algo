import sys
sys.stdin = open("인프런/Chapter[6]/input.txt",'r')

n , m = map(int,input().split())
li = [[0]*n for _ in range(n)]

for i in range(m):
    x, y, expense = map(int,input().split())
    li[x-1][y-1]=expense
for i in li:
    print(i)

