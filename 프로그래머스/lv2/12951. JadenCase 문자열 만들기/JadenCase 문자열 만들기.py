## 1차 시도
# def solution(s):
#     s = s.split(' ')
#     list = []
#     for i in range(0, len(s)):
#         list.append(s[i][0].upper() + s[i][1:].lower())
#     answer = ' '.join(list)
#     return answer

def solution(s):
    answer = s[0].upper() 
    for i in range(1, len(s)):
        if s[i-1] == " " and s[i] != " ":
            answer += s[i].upper() 
        else:
            answer += s[i].lower()
    return answer