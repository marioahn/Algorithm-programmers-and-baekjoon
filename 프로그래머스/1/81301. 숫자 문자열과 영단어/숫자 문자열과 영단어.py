def solution(s):
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for k in range(len(num)):
        arr = s.split(num[k])
        if len(arr) != 0:
            s = str(k).join(arr)
    
    return int(s)

print(solution("one4seveneight"))

# 레퍼런스 - wow;;;;;;;
# num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

# def solution(s):
#     answer = s
#     for key, value in num_dic.items():
#         answer = answer.replace(key, value)
#     return int(answer)