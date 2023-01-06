# https://putka-upm.acm.si/tasks/t/ceste/sl/

"""
Testni primeri:
test1.txt: Že napisan v nalogi
test2.txt: Pot s prvim najnižjim avtom ne bo dobra, ker je predraga
test3.txt: Pot s prvim najnižjim avtom ne bo dobra, ker je predolga
test4.txt. Nobena rešitev ne dobra (pričakujem -1)
"""

import heapq

ZACETNE_MAX_UTEZI = 10001
stevilo_primerov = int(input())


def rekonstrukcija_poti(seznam_predhodnikov, s, t):
    lst = [t]
    idx = t
    while seznam_predhodnikov[idx] is not None:
        lst.append(seznam_predhodnikov[idx])
        idx = seznam_predhodnikov[idx]
    return lst[::-1]


def mod_dijkstra(G, s, t, n):
    """Vrne minimalno visino avta, ki jo potrebujemo, da pridemo od vozlisca s do t na grafu G."""
    visited = [False] * (n + 1)
    cene_najkrajsih_poti = [False] * (n + 1)
    dolzine_najkrajsih_poti = [False] * (n + 1)
    max_utezi = [ZACETNE_MAX_UTEZI] * (n + 1)
    predhodnik = [None] * (n + 1)
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
                cene_najkrajsih_poti[v_i] = c_i + cene_najkrajsih_poti[u]
                dolzine_najkrajsih_poti[v_i] = d_i + dolzine_najkrajsih_poti[u]
                predhodnik[v_i] = u
    return max_utezi[t], dolzine_najkrajsih_poti[t], cene_najkrajsih_poti[t], rekonstrukcija_poti(predhodnik, s, t)


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
