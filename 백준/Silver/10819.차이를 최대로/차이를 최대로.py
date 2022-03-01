import sys
from itertools import permutations

n = int(sys.stdin.readline())
my_list = list(map(int, sys.stdin.readline().split()))
my_list = sorted(my_list)
answer = []

for i in permutations(my_list, n):
    cnt = 0
    for j in range(len(i)-1):
        cnt += abs(i[j] - i[j+1])
    answer.append(cnt)
    
print(max(answer))