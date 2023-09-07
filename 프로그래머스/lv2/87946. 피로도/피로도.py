from itertools import permutations 

def solution(k, dungeons):
    # dungeons: 행 길이 = 던전 개수
    # direction : 탐색 순서 (순열)
    answer = -1
    num_d = len(dungeons) 

    # 순열 이용해 탐색순서  
    for now_d in permutations(dungeons, num_d):
        tmp = k
        cnt = 0 
        
        for min_k, used_k in now_d : 
            if tmp >= min_k:
                tmp -= used_k 
                cnt += 1 
            else:
                pass 
        answer = max(cnt, answer)
        
    return answer