n, m, t = map(int, input().split())


mx = max(n, m)
mn = min(n, m)

cnt = 0
burger = 0
coke = 10000

while t >= mx*cnt:
    temp_t = t - mx*cnt
    temp_burger = cnt
    temp_coke = 0

    temp_burger += temp_t//mn
    temp_coke += temp_t%mn

    if coke > temp_coke:
        burger = temp_burger
        coke = temp_coke
    elif coke == temp_coke and burger < temp_burger:
        burger = temp_burger
        coke = temp_coke

    cnt += 1
    

print(f"{burger} {coke}")