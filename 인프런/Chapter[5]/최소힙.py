import sys
sys.stdin = open("인프런/Chapter[5]/input.txt",'r')
import heapq
heap = []
while True:
    num = int(input())
    if num==-1:
        break
    elif num==0:
        print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -num)
    