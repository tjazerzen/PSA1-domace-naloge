# Naloga 4: Ceste
# Tjaž Eržen, 27201009
# finančna matematika, 3. letnik

# https://putka-upm.acm.si/tasks/t/ceste/sl/

import heapq

ZACETNE_MAX_UTEZI = 10001
h_max = 10**6+1
stevilo_primerov = int(input())


def get_result_from_visited_dict(visited, t):
    visited_final_point_list = [tupple for tupple in visited.keys() if tupple[-1] == t]
    if not visited_final_point_list:
        return -1, -1, 1
    h, d, c, u = sorted(visited_final_point_list)[0]
    return h, d, c


def mod_dijkstra(G, s, t, C, D):
    """Vrne minimalno visino avta, ki jo potrebujemo, da pridemo od vozlisca s do t na grafu G."""
    visited = {}
    # Priority queue bo iz tupplov dolzine 4 oblike (h_i, d_i, c_i, u)
    pq = [(0, 0, 0, s)]  # Prvi argument predstavlja najmanjšo višino avta, da prečkamo reko
    while pq:
        h, d, c, u = heapq.heappop(pq)
        if visited.get((h, d, c, u), False):
            continue
        visited[(h, d, c, u)] = True
        for v_i, c_i, d_i, h_i in G[u]:
            if visited.get(v_i, False):
                continue
            if c + c_i <= C and d + d_i <= D:
                heapq.heappush(pq, (max(h, h_i), d+d_i, c+c_i, v_i))
    return visited


for _ in range(stevilo_primerov):
    input()
    n, m, s, t = map(int, input().strip().split(" "))
    C, D = map(int, input().strip().split(" "))
    seznam_sosednosti = {vozlisce: [] for vozlisce in range(1, n + 1)}
    for _ in range(m):
        u_i, v_i, c_i, d_i, h_i = map(int, input().strip().split(" "))
        seznam_sosednosti[u_i].append((v_i, c_i, d_i, h_i))
    visited_dict = mod_dijkstra(seznam_sosednosti, s, t, C, D)
    h, d, c = get_result_from_visited_dict(visited_dict, t)
    if h == -1:
        print(h)
    else:
        print(f"{h} {d} {c}")