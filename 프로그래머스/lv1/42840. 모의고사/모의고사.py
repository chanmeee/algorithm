def solution(answers):
    answer = []
    
    # 패턴 입력 
    pattern1 = [1,2,3,4,5]  # 5
    pattern2 = [2,1,2,3,2,4,2,5]  # 8
    pattern3 = [3,3,1,1,2,2,4,4,5,5]  # 10
    
    # 수포자별 정답 개수 세기 -> 나머지를 이용!  
    corr_num1, corr_num2, corr_num3 = 0, 0, 0
    for idx in range(len(answers)):
        
        if pattern1[idx % 5] == answers[idx]:
            corr_num1 += 1
        if pattern2[idx % 8] == answers[idx]:
            corr_num2 += 1
        if pattern3[idx % 10] == answers[idx]:
            corr_num3 += 1
    
    # 최대값 저장 후, 최대값이면 정답에 append 
    max_num = max(corr_num1, corr_num2, corr_num3)
    if max_num == corr_num1:
        answer.append(1)
    if max_num == corr_num2:
        answer.append(2)
    if max_num == corr_num3:
        answer.append(3) 
        
    return answer