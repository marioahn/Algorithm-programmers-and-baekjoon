# 1. 한칸 왼쪽으로 돌리는 함수
# 2. 올바른 괄호문자열인지 확인
    # 안되는 경우: 일단 짝이 안맞는경우 '}}'
    # 흠.. )(이렇게 거꾸로 붙어있는 경우는 어떻게 돌리던 안되는거같음
    # 그냥 앞에서부터 오프너 담아주고, 클로저들어왔을때 오프너랑 같이 없애지냐만 판별

def is_right(strs):
    bucket = []
    pair = {')': '(', '}': '{', ']': '['}

    if strs[0] in [')', '}', ']']:
        return False

    for str in strs:
        if str in ['(', '{', '[']: # 오프너면
            bucket.append(str)
        else: # 클로저면
            # 빈배열이면, bucket[-1] -> list index out of range에러
            if len(bucket) == 0 or bucket[-1] != pair[str]:
                return False
            else:
                del bucket[-1]
    
    if bucket == []: # 추가해줘야 함!
        return True
    else:
        return  False

def solution(s):
    cnt = 0

    # 1. 처음 상태(회전x)
    if is_right(s):
        cnt += 1
    
    # 2. 회전시작
    for _ in range(len(s)-1):
        s = s[1:] + s[0]
        if is_right(s):
            cnt += 1

    return cnt

print(solution("{([")) # 이거 0나와야 함 -> is_right함수 return값 수정


# 레퍼런스 - (), {}, []가 있으면 replace도 좋은 방법이네..오히려 간단한듯?
    # 조건도 덜 넣어도 되네;;
# from collections import deque

# def check(s):
#     while True:
#         if "()" in s: s=s.replace("()","")
#         elif "{}" in s: s=s.replace("{}","")
#         elif "[]" in s: s=s.replace("[]","")
#         else: return False if s else True       

# def solution(s):
#     ans = 0
#     que = deque(s)

#     for i in range(len(s)):
#         if check(''.join(que)): ans+=1
#         que.rotate(-1)
#     return ans