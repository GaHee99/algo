import sys
sys.stdin = open("인프런/Chapter[3]/input.txt",'r')

n,m = map(int,input().split())
li = list(map(int,input().split()))
start,end=0,0
count=0
while start <n and end <n:
    S = sum(list(li[start:end+1]))
    if S == m :
        count+=1
        end+=1
    elif S>m:
        start+=1
    elif S<m:
        end+=1
print(count)