from collections import Counter
from functools import reduce

def solution(clothes):
    # 의상 종류별 개수 세기
    counter = Counter([type for clothe, type in clothes])

    # 모든 종류의 count + 1을 누적해 곱
    answer = reduce(lambda acc, cur: acc*(cur+1), counter.values(), 1) - 1
    return answer

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))