
import sys
sys.stdin = open("인프런/Chapter[7]/input.txt")

number = list(map(int,input()))
numberList = []
for i in range(len(number)):
    numberList.append([])
print(numberList)

numberList[0].append(2)

def DFS(L):
    if L == len(number):
        print(numberList)
    else:   
        if len(numberList[L-1])==1:
            former = numberList[L-1][0]
            res = str(former)+str(number[L])
            if 1<=int(res)<=26:
                numberList[L-1].append(number[L])
                print(numberList)
                DFS(L+1)
        else:
            numberList[L-1].append(number[L])
            print(numberList)
            DFS(L+1)
                


DFS(1) # number[1] = 5
