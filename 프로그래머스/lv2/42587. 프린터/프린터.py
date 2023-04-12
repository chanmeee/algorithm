from collections import deque

def solution(priorities, location): 
    answer = 0
    # 인덱스 리스트를 생성 -> 이걸 stack으로 사용하기 
    my_doc = [0 for _ in range(len(priorities))] 
    my_doc[location] = 1 
    queue = deque(priorities) 
    # list(range()) 하면 0부터 n까지 리스트 생성됨, 하지만 list 대신 [] 기호 쓰면 생성 안 됨 !!!! 
    
    while True :
      # my_doc 비었거나, my_doc 에 목표 프린트의 인덱스가 없으면, loop 끝내기 
        if not my_doc or max(my_doc) == 0:
            break 
        # 최대값 = 첫값이면, 출력  / 대응되는 index도 제거 
        if max(queue) == queue[0] :
            queue.popleft()  # pop(0)보다는 popleft() 권장, 실행시간이 pop(0) 은 O(n)으로 리스트 크기에 따라 달라짐. 반면 덱의 popleft()는  O(1)의 빠른 복잡도로 원소 삭제가 가능 (front += 1 의 형태의 연산만을 수행하기 때문)
            del my_doc[0] 
            answer += 1     
            # 아니면, 첫값 빼내서 마지막에 넣기 
        else:
            queue.append(queue[0])
            queue.popleft()
            my_doc.append(my_doc[0])
            del my_doc[0]

    return answer 