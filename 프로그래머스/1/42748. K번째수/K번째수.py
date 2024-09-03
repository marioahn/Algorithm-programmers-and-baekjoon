def solution(array, commands):
    answer = []

    for k in range(len(commands)):
        slice_arr = array[commands[k][0]-1:commands[k][1]]
        slice_arr.sort()
        
        answer.append(slice_arr[commands[k][2]-1])

    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

# # 레퍼런스1
# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands)
          
# # 레퍼런스2
# def solution(array, commands):
#     return [sorted(array[a-1:b])[c-1] for a,b,c in commands]