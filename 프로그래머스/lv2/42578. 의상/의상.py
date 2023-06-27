from collections import Counter 
from functools import reduce 

def solution(clothes):
    answer = 0
    counts = Counter([kind for name, kind in clothes]) 

    answer = reduce(lambda x,y: x*(y+1), counts.values(), 1) -1 
    # reduce: 여러 개의 데이터를 누적 집계할 때 사용 
    ## reduce(집계함수, 반복 가능한 데이터, 초기값)
    # x 값에 y+1을 곱한다 (단 초기값 1) 
    
    return answer 