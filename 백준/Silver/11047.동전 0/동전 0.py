import sys

N, K = map(int, sys.stdin.readline().split())  # N: 동전 종류, K : 가치의 합

coin_lst = list()
for i in range(N):
    coin_lst.append(int(sys.stdin.readline()))

count = 0 
for i in reversed(range(N)):
    count += K//coin_lst[i] #카운트 값에 K를 동전으로 나눈 몫을 더해줌
    K = K%coin_lst[i] # K는 동전으로 나눈 나머지로 계속 반복

print(count)