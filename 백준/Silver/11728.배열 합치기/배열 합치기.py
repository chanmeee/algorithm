import sys 

n, m = map(int, sys.stdin.readline().split())
a_list = list(map(int, sys.stdin.readline().split()))
b_list = list(map(int, sys.stdin.readline().split()))

result = a_list + b_list
print (' '.join(map(str, sorted(result))))