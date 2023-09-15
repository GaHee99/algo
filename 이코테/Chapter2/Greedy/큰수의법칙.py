first_line = '5 8 3'
second_line = '2 4 5 4 6'

result = 0 
N, M, K = map(int, first_line.split())
number_list = list(map(int,second_line.split()))
number_list.sort(reverse=True)

# K번반복 
count = 0
for i in range(M):
    if count == K:
        result += number_list[1]
        count = 0
    else:
        result += number_list[0]
        count+=1
        
print(result)
