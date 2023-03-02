import sys
sys.stdin = open("인프런/Chapter[3]/input.txt",'r')

numbers = list(i for i in range(0,21))
for i in range(10):
    first, last = (map(int,input().split()))
    for k in range((last+1-first)//2):
        numbers[first+k], numbers[last-k] = numbers[last-k], numbers[first+k]
for i in range(1,21):
    print(numbers[i],end=' ')