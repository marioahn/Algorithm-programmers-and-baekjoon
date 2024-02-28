def solution(s):
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for k in range(len(num)):
        arr = s.split(num[k])
        if len(arr) != 0:
            s = str(k).join(arr)
    
    return int(s)



print(solution("one4seveneight"))