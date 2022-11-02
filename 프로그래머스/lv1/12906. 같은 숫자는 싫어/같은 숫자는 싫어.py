def solution(arr):
    answer = []
    if arr[0] == arr[-1]:
        answer.append(arr[0])
        
    for i in range(0,len(arr)):
        if arr[i] == arr[i-1]:
            continue            
        answer.append(arr[i])
    return answer