def solution(s, skip, index):
    # a ~ z / 단, skip꺼 빼고
    bucket = [chr(x) for x in range(97,123) if chr(x) not in skip]
    print(bucket)

    result = ''
    for ele in s:
        print(bucket.index(ele)+5)
        result += bucket[(bucket.index(ele)+index) % (len(bucket))]

    return result

print(solution("aukks","wbqd",5)) # happy