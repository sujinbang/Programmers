def solution(s):
    s = list(map(int, s.split(' ')))
    max_s = max(s)
    min_s = min(s)
    return str(min_s) + ' ' + str(max_s)