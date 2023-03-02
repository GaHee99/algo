import sys
# sys.stdin = open("인프런/Chapter[5]/input.txt",'r')
from collections import deque
def check(c):
    que = deque(must)
    for i in c:
        if i in must and i not in que:
            continue
        elif i in must and que.index(i)!=0:
            return False
        elif i in must and que.index(i)==0:
            que.popleft()
    if len(que)==0:
        return True

must = input()
num = int(input())
for i in range(num):
    c = input()
    if check(c):
        print("#%d YES"%(i+1))
    else:
        print("#%d NO"%(i+1))