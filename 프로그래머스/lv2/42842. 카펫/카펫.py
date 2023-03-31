# 가로 => 세로 
def solution(brown, yellow):
    answer = []
    total = brown+yellow
    for b in range(1, brown):

        if (total/b) %1 ==0:  # total=a*b
            a = total/b
            if a >= b:   
                if 2*a + 2*b == brown + 4: 
                    return [a,b]
    return answer

# 테스트
brown =10	
yellow=2
#[4, 3]

# (yellow 구역의 가로 길이) = a, 
# (yellow 구역의 세로 길이) = b 라 하면,
# a+b = (갈색 격자의 수 - 4) / 2
# axb = 노란색 격자의 수
# => b = (갈색 격자의 수 - 4) / 2 - a
# 2차방정식 2*a^2 + (4-갈색격자수)*a + 2*(노란격자수) = 0 을 만족하는 자연수 a를 찾는다. 식에서 자연수 a는 2*(노란격자수)의 약수임을 알수있다.


        
        
        
        

