# https://putka-upm.acm.si/tasks/t/vitez/

from collections import deque

stevilo_primerov = int(input())

R = ((1, 0), (0, 1), (-1, 0), (0, -1))


def veljavno(mreza, i, j):
    if i >= len(mreza) or i < 0 or j >= len(mreza[0]) or j < 0:  # out of range
        return False
    if mreza[i][j] == "#":  # zagrajeno
        return False
    return True


def sosedi(mreza, i, j):
    for dx, dy in R:
        if veljavno(mreza, i + dx, j + dy):
            yield i + dx, j + dy


def doloci_moci(mreza, w, h, zmaj_i, zmaj_j):
    moc = {}

    # Direktna polja
    if veljavno(mreza, zmaj_i, zmaj_j - 1):
        moc[(zmaj_i, zmaj_j - 1)] = 1
    if veljavno(mreza, zmaj_i, zmaj_j + 1):
        moc[(zmaj_i, zmaj_j + 1)] = 1
    if veljavno(mreza, zmaj_i - 1, zmaj_j):
        moc[(zmaj_i - 1, zmaj_j)] = 1
    if veljavno(mreza, zmaj_i + 1, zmaj_j):
        moc[(zmaj_i + 1, zmaj_j)] = 1

    # Kotna polja, do katerih pridemo do zmaja z enim korakom
    if veljavno(mreza, zmaj_i + 1, zmaj_j - 1):  # levo spodaj
        moc[(zmaj_i + 1, zmaj_j - 1)] = 2
    if veljavno(mreza, zmaj_i + 1, zmaj_j + 1):  # desno spodaj
        moc[(zmaj_i + 1, zmaj_j + 1)] = 2
    if veljavno(mreza, zmaj_i - 1, zmaj_j + 1):  # desno zgoraj
        moc[(zmaj_i - 1, zmaj_j + 1)] = 2
    if veljavno(mreza, zmaj_i - 1, zmaj_j - 1):  # levo zgoraj
        moc[(zmaj_i - 1, zmaj_j - 1)] = 2

    # Dolocanje moci napadov z leve strani
    if moc.get((zmaj_i - 1, zmaj_j - 1), None) and veljavno(mreza, zmaj_i - 1, zmaj_j - 2):
        for j in range(zmaj_j - 2, -1, -1):
            if mreza[zmaj_i - 1][j] == "#":
                break
            moc[(zmaj_i - 1, j)] = zmaj_j - j + 1
    if moc.get((zmaj_i, zmaj_j - 1), None) and veljavno(mreza, zmaj_i, zmaj_j - 2):
        for j in range(zmaj_j - 2, -1, -1):
            if mreza[zmaj_i][j] == "#":
                break
            moc[(zmaj_i, j)] = zmaj_j - j
    if moc.get((zmaj_i + 1, zmaj_j - 1), None) and veljavno(mreza, zmaj_i + 1, zmaj_j - 2):
        for j in range(zmaj_j - 2, -1, -1):
            if mreza[zmaj_i + 1][j] == "#":
                break
            moc[(zmaj_i + 1, j)] = zmaj_j - j + 1

    # Dolocanje moci napadov z desne strani
    if moc.get((zmaj_i - 1, zmaj_j + 1), None) and veljavno(mreza, zmaj_i - 1, zmaj_j + 2):
        for j in range(zmaj_j + 2, w):
            if mreza[zmaj_i - 1][j] == "#":
                break
            moc[(zmaj_i - 1, j)] = j - zmaj_j + 1
    if moc.get((zmaj_i, zmaj_j + 1), None) and veljavno(mreza, zmaj_i, zmaj_j + 2):
        for j in range(zmaj_j + 2, w):
            if mreza[zmaj_i][j] == "#":
                break
            moc[(zmaj_i, j)] = j - zmaj_j
    if moc.get((zmaj_i + 1, zmaj_j + 1), None) and veljavno(mreza, zmaj_i + 1, zmaj_j + 2):
        for j in range(zmaj_j + 2, w):
            if mreza[zmaj_i + 1][j] == "#":
                break
            moc[(zmaj_i + 1, j)] = j - zmaj_j + 1

    # Dolocanje moci napadov z zgornje strani
    if moc.get((zmaj_i - 1, zmaj_j - 1), None) and veljavno(mreza, zmaj_i - 2, zmaj_j - 1):
        for i in range(zmaj_i - 2, -1, -1):
            if mreza[i][zmaj_j - 1] == "#":
                break
            moc[(i, zmaj_j - 1)] = zmaj_i - i + 1
    if moc.get((zmaj_i - 1, zmaj_j), None) and veljavno(mreza, zmaj_i - 2, zmaj_j):
        for i in range(zmaj_i - 2, -1, -1):
            if mreza[i][zmaj_j] == "#":
                break
            moc[(i, zmaj_j)] = zmaj_i - i
    if moc.get((zmaj_i - 1, zmaj_j + 1), None) and veljavno(mreza, zmaj_i - 2, zmaj_j + 1):
        for i in range(zmaj_i - 2, -1, -1):
            if mreza[i][zmaj_j + 1] == "#":
                break
            moc[(i, zmaj_j + 1)] = zmaj_i - i + 1

    # Dolocanje moci napadov z spodnje strani
    if moc.get((zmaj_i - 1, zmaj_j - 1), None) and veljavno(mreza, zmaj_i + 2, zmaj_j - 1):
        for i in range(zmaj_i + 2, h):
            if mreza[i][zmaj_j - 1] == "#":
                break
            moc[(i, zmaj_j - 1)] = i - zmaj_i + 1
    if moc.get((zmaj_i + 1, zmaj_j), None) and veljavno(mreza, zmaj_i + 2, zmaj_j):
        for i in range(zmaj_i + 2, h):
            if mreza[i][zmaj_j] == "#":
                break
            moc[(i, zmaj_j)] = i - zmaj_i
    if moc.get((zmaj_i + 1, zmaj_j + 1), None) and veljavno(mreza, zmaj_i + 2, zmaj_j + 1):
        for i in range(zmaj_i + 2, h):
            if mreza[i][zmaj_j + 1] == "#":
                break
            moc[(i, zmaj_j + 1)] = i - zmaj_i + 1
    return moc


def bfs_najkrajse_poti(mreza, w, h, vitez_i, vitez_j, zmaj_i, zmaj_j):
    """Najde najkrajse poti od polozaja viteza do vseh ostalih polj."""
    sosedi_zmaja_in_zmaj = list(sosedi(grid, zmaj_i, zmaj_j)) + [(zmaj_i, zmaj_j)]
    q = deque([(vitez_i, vitez_j, 0)])
    dolzine_poti = {}
    visited = [[False for _ in range(w)] for _ in range(h)]
    while q:
        current_i, current_j, length = q.popleft()
        if visited[current_i][current_j]:
            continue
        dolzine_poti[(current_i, current_j)] = length
        visited[current_i][current_j] = True
        for sosed_i, sosed_j in sosedi(mreza, current_i, current_j):
            if sosed_i == zmaj_i and sosed_j == zmaj_j:
                continue
            if not visited[sosed_i][sosed_j]:
                q.append((sosed_i, sosed_j, length + 1))
    return dolzine_poti


def najdi_moc_napada(moci, najkrajse_poti, L):
    moci_list = list(moci.items())
    moci_list.sort(key=lambda x: x[1], reverse=True)
    for (moc_i, moc_j), moc_tega_napada in moci_list:
        # print((moc_i, moc_j), moc_tega_napada)
        if najkrajse_poti.get((moc_i, moc_j), L+1) + moc_tega_napada - 1 <= L:
            return moc_tega_napada
    return 0


for i in range(stevilo_primerov):
    input()
    w, h, L = map(int, input().strip().split(" "))
    grid = [[] for _ in range(h)]
    zmaj_i, zmaj_j, vitez_i, vitez_j = -1, -1, -1, -1
    for i in range(h):
        current_input = input().strip()
        for j in range(len(current_input)):
            char = current_input[j]
            if char == "V":
                vitez_i, vitez_j = i, j
            if char == "Z":
                zmaj_i, zmaj_j = i, j
            grid[i].append(char)
    moci = doloci_moci(grid, w, h, zmaj_i, zmaj_j)
    najkrajse_poti = bfs_najkrajse_poti(grid, w, h, vitez_i, vitez_j, zmaj_i, zmaj_j)
    moc_napada = najdi_moc_napada(moci, najkrajse_poti, L)
    print(moc_napada)
