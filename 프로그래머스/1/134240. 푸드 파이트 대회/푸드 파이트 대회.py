def solution(food):
    answer = ''

    left_str = ''
    for i in range(1,len(food)):
        left_str += str(i)*(food[i]//2)

    return left_str+'0'+left_str[::-1]