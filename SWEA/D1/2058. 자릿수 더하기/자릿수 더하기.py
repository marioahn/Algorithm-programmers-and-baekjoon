num = int(input())

new = list(map(int,[x for x in str(num)]))
print(sum(new))