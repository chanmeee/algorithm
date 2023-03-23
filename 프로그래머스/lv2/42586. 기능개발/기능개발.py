def solution(progresses, speeds):
    answer = [0] * 100
    time = 0 

    while len(progresses) >0:
        progresses = [p+s for p, s in zip(progresses, speeds)]
        
        for i in range(len(progresses)):
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                answer[time] +=1
        time += 1
    
    answer = [a for a in answer if a!=0]
    return answer