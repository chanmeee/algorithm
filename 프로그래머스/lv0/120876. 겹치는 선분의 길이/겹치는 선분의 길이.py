def solution(lines):
    answer = 0
    
    sets = [set(range(min(l), max(l))) for l in lines]
    print(sets)
    return len( sets[0]&sets[1] | sets[1]&sets[2] | sets[2]&sets[0] )
    
  