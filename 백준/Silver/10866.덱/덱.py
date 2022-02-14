import sys 

n = int(sys.stdin.readline())  # 명령어 개수  # 이전 문제 해답에서 뽀려옴

deque = []

for _ in range(n):
  order = sys.stdin.readline().split()

  if order[0] == 'push_front':
    deque.insert(0, order[1])  # insert(0, a): a를 맨 앞에 추가 
  elif order[0] == 'push_back':
    deque.append(order[1])

  elif order[0] == 'pop_front':
    if len(deque) == 0:  # 아무것도 없으면 
      print(-1)
    else:
      print(deque.pop(0))   # 그냥 pop 이 아님!!  
  elif order[0] == 'pop_back':
    if len(deque) == 0:  # 아무것도 없으면 
      print(-1)
    else:
      print(deque.pop())   # 그냥 pop 이 아님!! 

  elif order[0] == 'size':
    print(len(deque))

  elif order[0] == 'empty':
    if len(deque) == 0:  # 아무것도 없으면 
      print(1)
    else:
      print(0)
  elif order[0] == 'front':
    if len(deque) ==0:  # 아무것도 없으면 
      print(-1)
    else:
      print(deque[0])
  elif order[0] == 'back':
    if len(deque) ==0:  # 아무것도 없으면 
      print(-1)
    else:
      print(deque[-1])