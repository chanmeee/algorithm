def solution(answers):
    answer = []
    p1=[1,2,3,4,5] # -> [0,1,2,3,4] 
    p2=[2, 1, 2, 3, 2, 4, 2, 5]
    p3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5] 
    score=[0,0,0]
    
    for i, a in enumerate(answers) :
        # 수포자1 찍은 답안=정답이면,
        if p1[i % 5] == a: 
            score[0] +=1
        # 수포자2 
        if p2[i % 8] == a:
            score[1] +=1
        # 수포자3 
        if p3[i % 10] == a:
            score[2] +=1
            
    max_value = max(score) 
    answer=[i+1 for i, s in enumerate(score) if s==max_value] 
    
    return answer 