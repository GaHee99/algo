# 화폐의 종류만큼 반복 수행
# 따라서 화폐의 종류가 K개라고 할 때 시간 복잡도는 O(K)
# 큰 단위가 작은 단위의 배수이기 때문에 그리기가 가능


n = 1260
count = 0
coin_types = [500,100,50,10]

for coin in coin_types:
    count += n//coin
    n = n%coin
print(count)