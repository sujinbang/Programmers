def solution(n):
    answer = []
    str_n = str(n)
    for i in range(0,len(str_n)):
        answer.append(int(str_n[i]))
    answer.reverse()
    return answer