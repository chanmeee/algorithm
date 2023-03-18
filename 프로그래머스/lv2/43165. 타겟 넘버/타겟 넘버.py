# 2개 이상 20개 이하 -> DFS 해보자
# numbers: 사용할 수 있는 숫자가 담긴 배열
# target: 타겟 넘버 

from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer