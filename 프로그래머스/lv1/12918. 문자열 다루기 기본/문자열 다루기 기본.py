def solution(s):
    if len(s) == 4 and s.isdigit() == True:
        answer = True
    elif len(s) == 6 and s.isdigit() == True:
        answer = True
    else :
        answer = False
    return answer