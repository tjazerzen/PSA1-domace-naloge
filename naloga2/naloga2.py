# https://putka-upm.acm.si/tasks/t/podkupnine/

import sys

lines = sys.stdin.readlines()

stevilo_primerov = int(lines.pop(0).strip())  # map(int, lines.pop(0).strip().split(" "))
print(stevilo_primerov)

for _ in range(stevilo_primerov):
    lines.pop(0)  # Na začetku bomo imeli vedno prazno vrstico
    n, m, q, t = map(int, lines.pop(0).strip().split(" "))
    print(n, m, q, t)
    for _ in range(m):
        a_i, b_i, c_i = map(int, lines.pop(0).strip().split(" "))
        print(a_i, b_i, c_i)

# n, k, l = map(int, lines.pop(0).strip().split(" "))
