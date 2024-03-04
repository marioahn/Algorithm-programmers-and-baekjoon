def solution(X, Y):
    answer = ''

    # 이것도 시간복잡도 O(N**2)가 될 수 있지만, 이것 빼고는 1트 코드들 보다 훨씬 간결!
    for k in range(9,-1,-1):
        answer += str(k)*min(X.count(str(k)), Y.count(str(k)))

    if len(answer) == 0:
        return '-1'
    if answer[0] == '0':
        return '0'
    return answer