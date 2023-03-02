import sys
sys.stdin = open("인프런/Chapter[3]/input.txt",'r')

n = int(input())
first = list(map(int,input().split()))
m = int(input())
second = list(map(int,input().split()))
c= [] 
p1 = p2 = 0
while p1<n and p2<m:
    if first[p1]<second[p2]:
        c.append(first[p1])
        p1+=1
    else:
        c.append(second[p2])
        p2+=1
if p1<n:
    c=c+first[p1:]
if p2<m:
    c=c+second[p2:]
for x in c :
    print(x,end=' ')