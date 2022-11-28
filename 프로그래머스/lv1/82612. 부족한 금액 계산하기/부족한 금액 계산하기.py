def solution(price, money, count):
    answer = []
    
# 놀이기구 이용금액 (팩토리얼 기능 구현)
    for i in range(1, count+1):
        answer.append(price * i)
    sum_answer = sum(answer)

# 부족한 금액 출력
    if money > sum_answer:
        result = 0
    else :
        result = sum_answer - money

    return result