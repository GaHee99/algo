import sys
sys.stdin=open("인프런\Chapter[4]\input.txt", "r")
from collections import deque

n = int(input())
numbers = list(map(int,input().split()))
print(numbers)
left = numbers[0]
right = numbers[-1]
numbers =deque(numbers)
str = ""
count=0
last = 0 


print(count)
print(str)
