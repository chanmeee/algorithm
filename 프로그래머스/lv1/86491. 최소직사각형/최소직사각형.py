def solution(sizes):
    answer = 0
    
    max_list = []
    min_list = []

    for s in sizes:
        max_list.append(max(s))
        min_list.append(min(s))

    answer = max(max_list) * max(min_list)
    
    return answer