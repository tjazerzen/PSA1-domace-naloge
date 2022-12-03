# https://putka-upm.acm.si/tasks/t/vitez/

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


for _ in range(1):
    input()
    w, h, L = map(int, input().strip().split(" "))
    grid = []
    for _ in range(h):
        grid.append([char for char in input().strip()])
    print(grid)
