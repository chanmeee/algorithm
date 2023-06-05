n = input()

def answer(n):
  
  i = len(n)//2
  summation = 0 
  
  # 왼쪽 부분 더하기 
  for index in range(i):
    summation += int(n[index])
  # 오른쪽 부분 빼기 
  for index in range(i):
    summation -= int(n[index+i])
    
  # 왼쪽 = 오른쪽인지 검사 
  if summation ==0:
    return 'LUCKY' 
  else:
    return 'READY'

print(answer(n)) 