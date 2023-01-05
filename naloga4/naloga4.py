# https://putka-upm.acm.si/tasks/t/ceste/sl/

import heapq

ZACETNE_MAX_UTEZI = 10001
stevilo_primerov = int(input())


def mod_dijkstra(G, s, t, n):
    """Vrne minimalno visino avta, ki jo potrebujemo, da pridemo od vozlisca s do t na grafu G."""
    visited = [False]*(n+1)
    max_utezi = [ZACETNE_MAX_UTEZI]*(n+1)
    pq = [(0, s)]  # Prvi argument predstavlja najmanjšo višino avta, da prečkamo reko
    while pq:
        h, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        max_utezi[u] = h  # To bo pravilno nastavljeno, ker je to min kopica
        for v_i, c_i, d_i, h_i in G[u]:
            if not visited[v_i]:
                heapq.heappush(pq, (max(h, h_i), v_i))
    return max_utezi[t]


for _ in range(stevilo_primerov):
    input()
    n, m, s, t = map(int, input().strip().split(" "))
    C, D = map(int, input().strip().split(" "))
    seznam_sosednosti = {vozlisce: [] for vozlisce in range(1, n + 1)}
    for _ in range(m):
        u_i, v_i, c_i, d_i, h_i = map(int, input().strip().split(" "))
        seznam_sosednosti[u_i].append((v_i, c_i, d_i, h_i))
    minimalna_visina = mod_dijkstra(seznam_sosednosti, s, t, n)
    print(minimalna_visina)
