
M, N = [int(x) for x in input().split()]

type_counts = [0 for i in range(5)]
windows = list()
rlt = list()


for m in range(M):
    start = input()
    types = [0 for _ in range(N)]
    for i in range(4):
        windows = input().split("#")[1:-1]
        for idx, w in enumerate(windows):
            if w == "****":
                types[idx] += 1
    rlt.append(types)
end = input()

for r in rlt:
    type_counts[0] += r.count(0)
    type_counts[1] += r.count(1)
    type_counts[2] += r.count(2)
    type_counts[3] += r.count(3)
    type_counts[4] += r.count(4)

yeah = ' '.join([str(x) for x in type_counts])
print(yeah)