from collections import Counter

def solution(nums):
    answer = 0
    n = len(nums) 
    nums_c = Counter(nums) 
    answer = len(nums_c) 
    
    
    return n/2 if n/2 < answer else answer