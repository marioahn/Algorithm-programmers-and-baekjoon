def solution(s):
    mid_idx = len(s)//2
    
    return s[mid_idx] if (len(s) % 2 == 1) else s[mid_idx-1:mid_idx+1]