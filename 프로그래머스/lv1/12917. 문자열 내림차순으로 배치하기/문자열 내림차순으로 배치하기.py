def solution(s):
    sort_s = sorted(s)
    print(sort_s[0])
    print(len(sort_s))
    
    answer = ''
    for i in range(0,len(sort_s)):
        answer += sort_s[i]
    answer = answer[::-1]
    return answer