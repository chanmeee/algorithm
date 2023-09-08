# word 길이가 최대 5 => 완전탐색 가능 => 가능한 모든 조합 구하기 
# 중복조합 (중복 포함 5개 선택) 
from itertools import product 

def solution(word):
    answer = 0
    word_dict = []
    
    for i in range(1,6):  # 1,..,5개 중복선택 가능
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            word_dict.append(''.join(list(c))) 
    
    word_dict = sorted(word_dict)
    answer = word_dict.index(word) +1
    
    return answer