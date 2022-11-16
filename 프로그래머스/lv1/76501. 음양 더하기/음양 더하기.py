import math

def solution(absolutes, signs):
    answer = []
    for i in range(0, len(signs)):
        if signs[i] == True:
            answer.append(absolutes[i])
        else :
            absolutes[i] = -(absolutes[i])
            answer.append(absolutes[i])
            
    sum_answer = sum(answer)
    return sum_answer