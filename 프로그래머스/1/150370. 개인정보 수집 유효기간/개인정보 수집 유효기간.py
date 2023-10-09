# 시간 바꾸기
def time_convert(t):
    year,month,day = map(int, t.split('.'))
    return year*12*28 + month*28 + day
        
def solution(today, terms, privacies):
    answer=[]
    term_dict = dict()
    today = time_convert(today)
    
    # terms 기간을 일 단위 변경해 딕셔너리로 저장 
    for term in terms:
        name, period = term.split() 
        term_dict[name] = int(period)*28 
        
    for i, privacy in enumerate(privacies) :    
        start, name = privacy.split()
        # 유효기간 계산
        end = time_convert(start)+term_dict[name]
        # 오늘 일자와 비교 -> 파기여부 확인 
        if end <= today:
            answer.append(i+1)
        
    return answer 