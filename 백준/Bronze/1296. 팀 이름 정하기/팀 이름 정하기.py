from sys import stdin

name = stdin.readline().rstrip()
numOfTeam = int(stdin.readline().rstrip())
probList = []
for i in range(numOfTeam):
    teamName = stdin.readline().rstrip()
    s = name+teamName
    L = s.count("L")
    O = s.count("O")
    V = s.count("V")
    E = s.count("E")
    num = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    probList.append((num, teamName))
    
probList.sort(key=lambda x : (-x[0], x[1]))

print(probList[0][1])