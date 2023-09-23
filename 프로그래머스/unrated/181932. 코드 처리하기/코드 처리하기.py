def solution(code):
    ret = ''
    mode = 0
    
    for i, c in enumerate(code) :
        
        # 문자가 "1"이면 mode 변경 
        if c == '1':
            mode = 1-mode ## 1->0, 0->1
        
        else: 
            # mode가 0일 때 
            if mode==0:
                if c!='1' and i%2==0:
                    ret += c 
                elif c=='1':
                    mode = 1

            # mode가 1일 때 
            if mode==1:
                if c!='1' and i%2==1:
                    ret += c 
                elif c=='1':
                    mode = 0
        #print(i, c, mode, ret)        
    return 'EMPTY' if ret =='' else ret 