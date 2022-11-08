def solution(numbers):
    if sum(numbers) != 45:
        answer = 45 - sum(numbers)
    return answer