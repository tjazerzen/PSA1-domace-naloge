# https://putka-upm.acm.si/tasks/t/cevovod/

import heapq

stevilo_primerov = int(input())
ZACETNE_CENE_POTI = -10000*500*500*500


def najdrazja_pot_v_DAGu(seznam_sosednosti, cene_povezav, s, f):
    topoloska_ureditev = _toposort(seznam_sosednosti)
    V = len(seznam_sosednosti.keys())
    dist = {u: ZACETNE_CENE_POTI for u in seznam_sosednosti.keys()}
    dist[s] = 0
    for vozlisce in topoloska_ureditev:
        for sosed in seznam_sosednosti[vozlisce]:
            if dist[sosed] < dist[vozlisce] + cene_povezav[(vozlisce, sosed)]:
                dist[sosed] = dist[vozlisce] + cene_povezav[(vozlisce, sosed)]
    return dist[f] if dist[f] >= 1 else -1


def _toposort(seznam_sosednosti):
    """Grafu, ki ga predstavlja seznam sosednosti določi topološko ureditev"""
    n = len(seznam_sosednosti.keys())
    I = {i: 0 for i in range(1, n+1)}  # Stopnje vhodnih povezav
    for vozlisca, seznam_povezav in seznam_sosednosti.items():
        for vozlisce_out in seznam_povezav:
            I[vozlisce_out] += 1
    sklad = [u for u in range(1, n+1) if I[u] == 0]
    T = []
    while sklad:
        t = sklad.pop()
        T.append(t)
        for vozlisce_out in seznam_sosednosti[t]:
            I[vozlisce_out] -= 1
            if I[vozlisce_out] == 0:
                sklad.append(vozlisce_out)
    return T


for _ in range(stevilo_primerov):
    input()
    n, m = map(int, input().strip().split(" "))
    seznam_sosednosti = {vozlisce: [] for vozlisce in range(1, n+1)}
    cene_povezav = {}
    for _ in range(m):
        u_i, v_i, c_i = map(int, input().strip().split(" "))
        seznam_sosednosti[u_i].append(v_i)
        cene_povezav[(u_i, v_i)] = c_i
    s, f = map(int, input().strip().split(" "))
    # toposort_rezultat = _toposort(seznam_sosednosti)
    # print(toposort_rezultat)
    najdrazje_poti = najdrazja_pot_v_DAGu(seznam_sosednosti, cene_povezav, s, f)
    print(najdrazje_poti)
