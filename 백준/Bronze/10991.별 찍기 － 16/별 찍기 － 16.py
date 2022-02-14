n = int(input())

for _ in range(n):
    print(' '*list(reversed(range(n)))[_] + ' '.join('*'*(_+1)))  # 왜 RuntimeError가 발생하는 건지 모르겠음!