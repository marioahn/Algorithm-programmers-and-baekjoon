# 중복"순열"로 풀거나 규칙찾아서 하면 될것 같긴 한데,
# 일단 완전탐색으로 재활 & 연습겸 ㄱㄱ
# 먼저, void, A, E, I, O, U 순으로 붙인다고 생각하면 될듯
    # void만나게 되면 그 뒷자리에 더이상 붙일 수 없음(void가 A보다 먼저임)
        # if now[-1] == 'x': return
    # 이때, return시키고, return하기 직전에 answer+=1해서 번호 세면 될듯
    # 그리고, 마지막으로 now의 길이가 5에 도달하게 되면 마찬가지로 return & +=1
# * -> ㄴㄴ. 'x'필요없음.. 애초에 너무 복잡하게 생각했음. bfs아니고, dfs임. - 재활 확실히 했네
    # bool값 이용하기.
# ---
answer = 0
def dfs(sum, target):
    global answer # 이걸 써줘야, bfs함수 밖에 있는 answer변수와 여기 answer가 연동
    answer += 1

    if sum == target:
        return True
    if len(sum) == 5: # 여기까지 왔는데도 못찾으면 False하고 다른거 찾아
        return False
    
    vowels = ['A', 'E', 'I', 'O', 'U']
    for vowel in vowels:
        if dfs(sum+vowel, target): # True면
            return True


def solution(word):
    global answer
    # 아예 밖에서부터 하나 미리 주고 시작하는것도 괜찮은듯.ㅇㅇ
    vowels = ['A', 'E', 'I', 'O', 'U']
    for vowel in vowels:
        if dfs(vowel, word): # True면
            return answer

# 참고로 이 전체 코드에서 아래 print문을 쭉 실행시키면 결과값이 정답과 다르게 나온다
# 왜냐? answer 는 전역변수로서 맨 위에 선언되어있고, 각 print문이 한번 실행될때마다 answer가 0이 아니라,
    # 변화된 상태에서 또 새로 시작하기 때문이다.
    # *이 점. 주의.....
# print(solution("A"))
# print(solution("AA"))
# print(solution("AAAE")) 
# print(solution("AAAAE"))
# print(solution("I"))