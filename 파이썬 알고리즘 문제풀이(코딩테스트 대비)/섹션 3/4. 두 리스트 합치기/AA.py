import sys
# sys.stdin = open("인프런/Chapter[3]/input.txt",'r')

n = int(input())
first = list(map(int,input().split()))
m = int(input())
second = list(map(int,input().split()))
res = first+second
res.sort()
for i in res:
    print(i, end=' ')