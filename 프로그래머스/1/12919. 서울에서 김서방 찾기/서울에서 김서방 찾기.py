# def solution(seoul):
#     idx = 0
#     # for i in range(0,len(seoul)):
#     #     if seoul[i] == 'Kim':
#     #         idx = i
#     #         break
#     idx = seoul.index('Kim')
    
#     return f'김서방은 {idx}에 있다'

def solution(seoul):
    idx = 0
    for i in range(0,len(seoul)):
        if seoul[i] == 'Kim':
            idx = i
            break
    
    return f'김서방은 {idx}에 있다'