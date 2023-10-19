n = int(input())
a = ['Algorithm', 'DataAnalysis', 'ArtificialIntelligence',
     'CyberSecurity', 'Network', 'Startup', 'TestStrategy']
b = [204, 207, 302, 'B101', 303, 501, 105]

for _ in range(n):
    x = input()
    print(b[a.index(x)])
