num = int(input())
li = list()
for i in range(num):
    li.append(int(input()))
print(sorted(li,reverse=True))