# 참조: https://latte-is-horse.tistory.com/146
def solution(rows, columns, queries):
    answer = []
    table =[[col+row*columns+1 for col in range(columns)] for row in range(rows)]

    for query in queries:
        query = [x-1 for x in query] # idx에 맞게 설정
        tmp = table[query[0]][query[1]] # 왼쪽위부터 시작할 것이기에, 초기값 저장
        small = tmp

        # 1. left
        for i in range(query[0]+1, query[2]+1):
            table[i-1][query[1]] = table[i][query[1]]
            small = min(small, table[i][query[1]])
        # 2. bottom
        for i in range(query[1]+1, query[3]+1):
            table[query[2]][i-1] = table[query[2]][i]
            small = min(small, table[query[2]][i])
        # 3. right
        for i in range(query[2]-1, query[0]-1, -1):
            table[i+1][query[3]] = table[i][query[3]]
            small = min(small, table[i][query[3]])
        # 4. top
        for i in range(query[3]-1, query[1]-1, -1):
            table[query[0]][i+1] = table[query[0]][i]
            small = min(small, table[query[0]][i])

        
        table[query[0]][query[1]+1] = tmp
        answer.append(small)
    
    return answer

    