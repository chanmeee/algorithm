
# 다른 사람 풀이 
def solution(participant, completion):
    
    answer = ''
    temp = 0
    dic = {}
    
    for part in participant:
        dic[part] = hash(part)
        temp += hash(part) 
    for com in completion:
        temp -= hash(com)
    answer = [k for k, v in dic.items() if v==temp][0]

    return answer 