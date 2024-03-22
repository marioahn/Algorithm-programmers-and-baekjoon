# 제한사항: 5 ≤ sequence의 길이 ≤ 1,000,000
# 합이 k인 부분 수열이 여러 개인 경우 길이가 짧은 수열을 찾는다
# 길이가 짧은 수열이 여러 개인 경우 앞쪽(시작 인덱스가 작은)에 나오는 수열을 찾는다

# 이것도 stack을 이용해서 풀어야 할듯
    # 단, start, end 2개의 idx 변수들을 저장하면 될듯
    # 이렇게 저장된 것중에서 길이가 같은거면 맨 앞에 있는 것 골라내면 되니까
    # 그렇다면, idx조합을 어떻게 stack으로 추출해낼 것인가?

# *오름차순이 힌트가 될 것 같음 -> 결과적으로 투 포인트면 상관없을 듯 하다
    # *과연 그런가? '정렬'이 안된 상태였으면? -> ㄴㄴ 큰 차이는 없음
# 아. 누적합 이용하면 될것 같은데? 흠..
# 일단 start가 다른 누적합(i=0,1,...n-1)들 구해서 해보자
    # 근데 이러면 어차피 시간복잡도 O(N**2)일것 같은데..

# 투포인터 느낌으로  스택 채워가면 될것 같은데. 이때, 값과 인덱스 같이 저장해줘야 함
# sequence 포문돌면서 하나씩 추가하고, SUM추가 및 K 초과하면 앞에꺼 빼고 SUM빼고
# https://velog.io/@sugyeonghh/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%97%B0%EC%86%8D%EB%90%9C-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4%EC%9D%98-%ED%95%A9Python
    # 내 구상이 맞긴 했으나, 구현을 못함. 요즘 너무 구현력 떨어진듯
    # 처음엔 for문으로 시작했으나 while문이 더 적절했음
# 마지막으로 길이 비교하면서 더 짧은 인덱스 보이면 앞에 걸로 ㄱㄱ
    # 또한, 길이가 같은 idx면 갱신x(맨 앞 인덱스로 해야 하므로)

def solution(sequence, k):
    left, right, sum, = 0, 0, sequence[0] # 초기값 세팅
    result = [0,len(sequence)] # 각idx는 각각 left, right / 작은 stack느낌

    while 1:
        if sum < k:
            right += 1
            if right == len(sequence):
                break # poin
            sum += sequence[right]
        else: # sum >= k
            if sum == k and (result[1]-result[0] > right-left):
                result = [left, right]
            sum -= sequence[left]
            left += 1
    
    return result

print(solution([1,2,3,4,5],7)) # [2,3]
print(solution([1, 1, 1, 2, 3, 4, 5],5)) # [6,6]
print(solution([2, 2, 2, 2, 2],6)) # [0,2]
