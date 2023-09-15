

row, column = map(int, input().split())
result = 0
for i in range(row):
    per_row = list(map(int,input().split()))
    result = max(min(per_row), result)

print(result)
