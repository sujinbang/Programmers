def solution(my_string, letter):
    # 특정 문자 삭제 : strip()
    # 숫자형은 remove()로 삭제 가능
    answer = ''
    for i in range(0,len(my_string)):
        if my_string[i] == letter:
            continue
        answer += my_string[i]
    return answer