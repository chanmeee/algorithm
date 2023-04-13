from collections import deque 

def solution(bridge_length, weight, truck_weights):
    time = 0
    wait = deque(truck_weights)  # 대기 중인 트럭 무게를 deque로 만들기 
    bridge = deque([0] * bridge_length)  # 다리 상황을 [0,..,0] deque로 마들기 
    sum_weight = 0  # 현재 다리의 무게 --- 예제1개 시간초과  
    
    while bridge :
        
        time += 1 
        
        # 나갈 트럭 있으면, 해당 무게를 '현재 다리무게'에서 빼기
        if bridge[0] != 0 :
            sum_weight -=bridge[0] 
        bridge.popleft() # popleft() 쓰려면, list는 불가하고 deque() 써야함 
        
        if wait:
            # 허용무게 초과 안하면, 다리에 대기1번트럭 추가 
            if (sum_weight + wait[0]) <= weight :
                sum_weight += wait[0]  # 무게 추가 
                bridge.append(wait.popleft()) 
                
            # 초과 했으면, 0 추가 
            else:
                bridge.append(0) 

    return time