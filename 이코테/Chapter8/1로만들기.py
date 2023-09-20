# 정수 x 입력받기 
x = int(input())

d = [0] * 30


# 다이나믹 프로그래밍 보텀업
for i in range(2, x+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1

    # 2로 나누어 떨어질 경우 
    if i%2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    
    # 3으로 나누어 떨어질 경우
    if i%3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    
    if i%5 == 0:
        d[i] = min(d[i], d[i//5]+1)
    print(i, d[i])
print(d)
print(d[x])