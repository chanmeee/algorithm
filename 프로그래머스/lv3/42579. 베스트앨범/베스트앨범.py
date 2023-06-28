def solution(genres, plays):
    answer = []
    dict1 = {}   # 장르: (노래 번호, 노래 재생수)
    dict2 = {}   # 장르: 총 재생수
    
    # 1) dict 2개 만들기: 값 [총 재생수, [노래 재생수, 노래번호], ...]
    for i, (g, p) in enumerate(zip(genres, plays)) :
        if g in dict1:
            dict1[g].append((i,p))  # (노래1 번호, 노래1 재생수)
        else:
            dict1[g] = [(i,p)]  
            
        if g in dict2:
            dict2[g] += p
        else:
            dict2[g] = p 
    
    # 2) 장르: 총 재생수 기준 내림차순 정렬 
    for (k, _) in sorted(dict2.items(), key=lambda x: x[1], reverse=True):
        # 3) 노래: 재생수 기준 내림차순 + 고유번호 기준 오름차순 & 최대 2개 
        for (i, p) in sorted(dict1[k], key=lambda x: (x[1], -x[0]),reverse=True)[:2]:
            #print(p)
            answer.append(i) 
    
    #print(dict2)
    #print(dict1)
        
    return answer