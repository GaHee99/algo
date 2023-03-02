import sys
# sys.stdin=open("인프런\Chapter[5]\input.txt", "r")
from collections import deque
number , m = map(str,input().split())
m = int(m)


stack = []
stack.append(int(number[0]))
i=1
for i in range(1, len(number)):
    if stack and int(number[i])>stack[-1] and m>0:
        while stack and int(number[i])>stack[-1] and m>0:
            stack.pop()
            m-=1
    stack.append(int(number[i]))
if m>0:
    for i in range(m):
        stack.pop()
res = ""
for i in stack:
    res+=str(i)

print(res)
    