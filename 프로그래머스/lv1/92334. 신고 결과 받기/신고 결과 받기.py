def solution(id_list, report, k):
    report = list(set(report))  # 중복 신고 제거
    answer = [0] * len(id_list)
    r_dict = {i:0 for i in id_list} 
    
    for r in report:
        r_dict[r.split()[1]] +=1 
    
    for r in report:
        if r_dict[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] +=1
    
    return answer