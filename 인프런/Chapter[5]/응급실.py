import sys
sys.stdin = open("인프런/Chapter[5]/input.txt",'r')
from collections import deque

n, m = map(int,input().split())
list = list(map(int,input().split()))
patientList=[]
for i in range(len(list)):
    patientList.append((i, list[i]))
que = deque(patientList)
count = 0 
while True:
    index, dangerous = que.popleft()
    if any(dangerous< dan  for (ind,dan) in que):
        que.append((index,dangerous))
    else:
        if index == m :
            count+=1
            print(count)
            sys.exit(0)
        else:
            count+=1


