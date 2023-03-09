# participant: 참여 선수 이름이 담긴 배열 
# completion : 완주 선수 이름 
# 완주하지 못한 선수의 이름 반환 

# from collections import Counter 
# def solution(participant, completion):

#     diff = Counter(participant) - Counter(completion)
  
#     answer = list(diff)[0]
#     return answer 

# def solution(participant, completion):
    
#     answer = ''
    
#     for idx in range(len(participant) - 1):
#         if completion[idx] != participant[idx]:
#             answer = participant[idx] 
    
#     return answer 



# 다른 사람 풀이 
def solution(participant, completion):
    
    answer = ''
    temp = 0
    dic = {}
    
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer 