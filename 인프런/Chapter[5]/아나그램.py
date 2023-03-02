import sys
sys.stdin = open("인프런/Chapter[5]/input.txt",'r')
from collections import deque

first = list(map(str,input()))
second = list(map(str,input()))

for f in first:
    if f in second:
        second.remove(f)

if len(second)==0:
    print("YES")
else:
    print("NO")