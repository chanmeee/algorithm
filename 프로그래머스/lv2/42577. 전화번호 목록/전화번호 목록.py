# 전화번호를 담은 배열 phone_book
def solution(phone_book):
    
    answer = True 
    phone_book.sort()  # 글자순 정렬

    for i in range(1,len(phone_book)) :
        if phone_book[i].startswith(phone_book[i-1]):
            answer = False
    
    return answer