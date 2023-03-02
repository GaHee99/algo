import sys
# sys.stdin=open("인프런\Chapter[4]\input.txt", "r")
from collections import deque
# 2명이하, Mkg 이하 
n,m = map(int,input().split())
people = list(map(int,input().split()))
people.sort(reverse=True)
people=deque(people)
count=0
while people:
    f = people.popleft()
    if len(people)>0 and (f + people[-1])<=m:
        people.pop()
    count+=1
print(count)
