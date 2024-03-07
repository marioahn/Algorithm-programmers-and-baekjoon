# 피보나친데? 왜 피보나치가 되는 거였더라;;

def solution(n):
    fibo_run = [1,2]

    a,b = 1,2
    if n>=3:
        for k in range(n-2):
            fibo_run.append(a+b)
            a, b = b, a+b
        return fibo_run[n-1] %(1234567)
    else:
        return fibo_run[n-1]
    