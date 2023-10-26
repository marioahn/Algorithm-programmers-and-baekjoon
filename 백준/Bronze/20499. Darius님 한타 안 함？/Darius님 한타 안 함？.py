kda = input()

K, D, A = kda.split('/')
K, D, A = int(K), int(D), int(A)

if (K+A) < D or D == 0:
    print('hasu')
else:
    print('gosu')
