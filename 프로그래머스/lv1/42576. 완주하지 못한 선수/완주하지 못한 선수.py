def solution(participant, completion):
    answer = ''
    from collections import Counter

    answer=list((Counter(participant) - Counter(completion)).elements() ).pop()

    return answer