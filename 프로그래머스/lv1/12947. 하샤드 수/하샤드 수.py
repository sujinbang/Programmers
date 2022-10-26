def solution(x):
    str_x = str(x)
    list = []
    for i in range(0,len(str_x)):
        list.append(int(str_x[i]))
    sum_x = sum(list)  # 자릿수의 합
    
    if x % sum_x == 0:
        answer = True
    else :
        answer = False
    return answer