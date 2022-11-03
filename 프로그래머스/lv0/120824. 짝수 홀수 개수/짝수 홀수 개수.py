def solution(num_list):
    num1 = []
    for i in num_list:
        if i % 2 == 0:
            num1.append(1)
    num2 = []
    for i in num_list:
        if i % 2 != 0:
            num2.append(1)
    num1 = sum(num1)
    num2 = sum(num2)
    answer = []
    answer.append(num1)
    answer.append(num2)
    return answer