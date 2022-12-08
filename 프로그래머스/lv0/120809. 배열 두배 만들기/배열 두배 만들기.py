def solution(numbers):
    answer = []
    for i in range(0, len(numbers)):
        num = numbers[i] * 2
        answer.append(num)
    return answer