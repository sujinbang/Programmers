def solution(arr1, arr2):
    answer = []
    
    for i in range(0, len(arr1)):
        arr_sum = []
        for j in range(0, len(arr1[0])):
            arr_sum.append(arr1[i][j] + arr2[i][j])
        answer.append(arr_sum)
    
    # print([arr1[0][0]+arr2[0][0]])
    # print([arr1[1][0]+arr2[1][0]])
    return answer

    