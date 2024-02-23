def solution(absolutes, signs):
    result = 0
    for i in range(len(absolutes)):
        if signs[i] == False:
            result += -(absolutes[i])
        else:
            result += absolutes[i]
            
    return result  

# 한 줄 코딩 생각해봤는데 잘 안되었음 -> 아래 참고 굿
# for문, if문과 2개 변수를 동시에 사용하는 방법
# return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))


