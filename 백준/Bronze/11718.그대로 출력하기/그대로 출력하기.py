# 최대 100줄
# 알파벳 소문자, 대문자, 공백, 숫자로만

while True :
    try :
        print(input())
    except EOFError:  # EOFError: 입력값이 안들어온다면, 즉 EOF(End Of File)상태
        break