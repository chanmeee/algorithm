def solution(citations):
    answer = 0
    
    citations = sorted(citations, reverse=True) # 숫자 역순 정렬
    for idx, c in enumerate(citations) : # h의 최댓값 탐색 
        if idx >= c:   # 2 < 6 | 3<5 | 4 > 3
            return idx  # return: 함수를 종료시킴  
        
    return len(citations) 

# citations = [3,3, 0, 4, 6, 1, 5, 4]  
# answer = 0 
# # ========================== 
# citations = sorted(citations, reverse=True) # 숫자 역순 정렬

# # c : [6,5,4,4,3,3,1,0] 
# # idx : [0,1,2,3,4,5,6,7,8] 

# for idx, c in enumerate(citations) :
#     # print(idx+1, c)
#     if idx >= c:   # 2 < 6 | 3<5 | 4 > 3
#         return idx
    
# print(len(citations))
     
#     # if (idx+1) >= c:   # 2 < 6 | 3<5 | 4 > 3
#     #     answer=c 
#     #     break 

# # print(answer) 
