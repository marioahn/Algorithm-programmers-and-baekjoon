# 매번 쪼개질때마다 4개로 쪼개지고,
# 1사분면, 2사분면, 3사분면, 4사분면으로 나뉘는 각 코드 구성
# 직접 코드를 짜야 하나? 너무 비효율적인거 같은데.. 일단 풀고 레퍼런스 ㄱㄱ
# 재귀로 계속 들어가야 할듯: 1024=2**10. arr의 길이 
# import math # print(int(math.log2(1024)))
def solution(arr):
    result=[0,0]
    length=len(arr)
    
    def dfs(a,b,l):
        start=arr[a][b]
        for i in range(a,a+l):
            for j in range(b,b+l):
                if arr[i][j]!=start:
                    l=l//2
                    dfs(a,b,l)
                    dfs(a,b+l,l)
                    dfs(a+l,b,l)
                    dfs(a+l,b+l,l)
                    return
                
        result[start]+=1
        
    dfs(0,0,length)
    
    return (result)

