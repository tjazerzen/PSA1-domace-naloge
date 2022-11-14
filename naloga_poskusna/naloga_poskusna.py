# https://putka-upm.acm.si/tasks/t/ceska/

import sys


def prefix_sums(l):
    ps = [0]
    cs = 0
    for i in l:
        cs += i
        ps.append(cs)
    return ps


lines = sys.stdin.readlines()  # open("test.txt", "r").readlines()

n, k, l = map(int, lines.pop(0).strip().split(" "))


lines.pop(0)  # na�a ekipa, ime ni pomembno tako da lahko presko�imo to vrstico

team_sums = []  # prefix sums za vse ekipe

our_efficiency = map(int, lines.pop(0).strip().split(" "))

our_prefix = prefix_sums(our_efficiency)  # nase prefix vsote

# prefix sums izracunamo za vse ekipe
for _ in range(l - 1):
    lines.pop(0)  # team name
    team_sums.append(prefix_sums(map(int, lines.pop(0).strip().split(" "))))

## za vsak mo�ni k_0 izracunamo na�e mesto
nm = l  ## nase mesto, ziher bo manjse ali enako kot to

for k0 in range(k, n + 1):

    # izra�unamo nase mesto za izbran k0
    our_place = l
    our_score = our_prefix[n] - our_prefix[k0] + our_prefix[k0 - k]

    for t in team_sums:
        t_score = t[n] - t[k0] + t[k0 - k]
        if our_score >= t_score:
            our_place -= 1

    # preverimo ce smo boljsi kot za prejsnje k_0
    if our_place < nm:
        nm = our_place

# vrnemo samo eno stevilo, torej nase mesto

print(nm)
