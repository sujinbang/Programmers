def solution(left, right):
    answer = []
    for i in range(left, right+1):
        # 약수의 개수
        list = []
        for j in range(1, i+1):
            if i % j == 0:
                list.append(1)
        # 약수의 개수가 짝수인지 홀수인지
        if sum(list) % 2 == 0:
            answer.append(i)
        else :
            answer.append(-i)
    sum_answer = sum(answer)
    return sum_answer