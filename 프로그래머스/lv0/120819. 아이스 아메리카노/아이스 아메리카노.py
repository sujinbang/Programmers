def solution(money):
    cnt = money // 5500
    remain = money % 5500
    answer = []
    answer.append(cnt)
    answer.append(remain)
    return answer