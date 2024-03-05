# 그냥 A-Z까지, 최소횟수 나타내는 dict 만들어서,
# targets순회하면서 value값들 추가하면 될듯
def solution(keymaps, targets):
    dict = {}
    for keymap in keymaps:
        for k in range(len(keymap)):
            if keymap[k] not in dict:
                dict[keymap[k]] = k+1
            else:
                dict[keymap[k]] = min(k+1, dict[keymap[k]])
    
    answer = []
    for target in targets:
        cnt = 0
        for word in target:
            if word in dict:
                cnt += dict[word]
            else:
                answer.append(-1)
                cnt = 0 # 초기화 안 시키면, 아래 코드에서 안 걸러짐
                        # 반례: ["ABCE"],["ABDE"] -> [-1, 3]이 나와버림
                break

        if cnt != 0:
            answer.append(cnt)

    return answer


print(solution(["ABACD","BCEFD"],["ABCD","AABB"]))
print(solution(["AA"],["B"]))
print(solution(["AGZ","BSSS"],["ASA","BGZ"]))
print(solution(["BC"],["AC", "BC"])) # 아. [-1, 3]가 나와야 함..
print(solution(["ABCE"],["ABDE"])) # [-1]이 나와야 함