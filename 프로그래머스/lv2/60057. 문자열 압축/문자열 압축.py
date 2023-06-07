def solution(s):
    answer = len(s)
    
    # 1 ~ n/2 모든 수를 단위로 하여 문자열을 압축하는 방법을 찾아본다
    # 그 중 가장 짧게 압축되는 길이를 리턴 

    for step in range(1,len(s)//2 +1):
        compressed =''
        prev = s[:step]
        count =1
        # 단위(step)만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전과 동일하면, count를 +1
            if prev == s[j:j+step]:
                count +=1
            # 이전과 다르면 (더이상 압축이 안되면)
            else:  
                compressed += str(count) + prev if count>=2 else prev
                prev = s[j:j+step]  # prev 초기화 
                count=1  # count 초기화 
                
        # 남아있는 문자열 처리
        compressed += str(count)+prev if count>=2 else prev
        
        # 가장 짧은 압축문자열 반환 
        answer = min(answer, len(compressed))

    
    return answer