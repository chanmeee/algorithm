def solution(array, commands):
    answer = []
    
    for c in commands:
        
#         # 자르기 
#         print(array[(c[0]-1):c[1]])
        
#         # 정렬 
#         print(sorted(array[(c[0]-1):c[1]]) )

#         # 인덱싱 
#         print(sorted(array[(c[0]-1):c[1]])[c[2]-1]) 
        
        answer.append( sorted(array[(c[0]-1):c[1]])[c[2]-1] )
    
    return answer