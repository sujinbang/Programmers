def solution(n):
    str_n = str(n)
    str_n = sorted(str_n, reverse=True)
    answer = int(''.join(str_n))
    return answer

# list(map(int, answer)) -- 리스트 안의 문자열을 정수로