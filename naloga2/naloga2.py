# https://putka-upm.acm.si/tasks/t/podkupnine/

import sys
from functools import lru_cache

stevilo_primerov = int(input())

@lru_cache(None)
def vsota_geom_zaporedja_rec(potenca, q, t):
    if potenca == 0:
        return 1
    if potenca % 2 == 0:
        return (vsota_geom_zaporedja_rec(potenca//2, q, t) + pow(q, potenca // 2 + 1, t) * vsota_geom_zaporedja_rec(potenca // 2 - 1, q, t)) % t
    else:
        return ((1 + pow(q, (potenca + 1) // 2, t)) * vsota_geom_zaporedja_rec(potenca // 2, q, t)) % t


for _ in range(stevilo_primerov):
    input()
    n, m, q, t = map(int, input().strip().split(" "))
    vrednost = 0
    for _ in range(m):
        a_i, b_i, c_i = map(int, input().strip().split(" "))
        # vrednost += c_i * pow(q, a_i-1, t) * (((1-q**(b_i-a_i+1)) // (1-q)) % t)
        vrednost += c_i * pow(q, a_i - 1, t) * vsota_geom_zaporedja_rec(b_i - a_i, q, t)
        vrednost = vrednost % t
    print(vrednost)
