import sys
sys.stdin = open("인프런/Chapter[6]/input.txt",'r')
from collections import deque
n,m = map(int,input().split())
Map = [[0]*n for _ in range(n)]
que=deque()
leftover=[]
for i in range(m):
    start,end = map(int,input().split())
    if start ==1 :
        que.append((start,end))
    else:
        leftover.append((start,end))
    Map[start-1][end-1]=1
count=0
log = [] 
while que:  
    start, end = que.popleft() # start은 무조건 1 
    log.append(start)
    while True:
        for i in leftover:
            l_start, l_end = i
            if l_end in log: # 무한루프 
                continue
            elif l_end not in log and end == l_start:
                start=l_start
                end = l_end
                log.append(start)
                if end == 5:
                    count+=1
                    print(log)
                    log=[1]
                    continue
                
                    
    

