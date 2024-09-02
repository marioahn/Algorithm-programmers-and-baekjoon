def solution(s):
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for k in range(len(num)):
        s = s.replace(num[k], str(k))  # num[k]에 해당하는 영단어를 k로 대체
    
    return int(s)  # 최종적으로 변환된 문자열을 정수로 변환하여 반환

print(solution("one4seveneight"))


# 레퍼런스 - wow;;;;;;;
# num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

# def solution(s):
#     answer = s
#     for key, value in num_dic.items():
#         answer = answer.replace(key, value)
#     return int(answer)