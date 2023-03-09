# participant: 참여 선수 이름이 담긴 배열 
# completion : 완주 선수 이름 
# 완주하지 못한 선수의 이름 반환 

from collections import Counter 
def solution(participant, completion):

    diff = Counter(participant) - Counter(completion)
  
    answer = list(diff)[0]
    return answer 