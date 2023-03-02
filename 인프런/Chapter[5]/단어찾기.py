import sys
# sys.stdin = open("인프런/Chapter[5]/input.txt",'r')
from collections import deque

n = int(input())
word=[]
for i in range(n):
    word.append(input())
for i in range(n-1):
    english = input()
    if english in word :
        word.remove(english)
print(word[0])