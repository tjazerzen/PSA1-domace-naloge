# https://putka-upm.acm.si/tasks/t/typo/

from functools import lru_cache
from copy import deepcopy


def lev_dist_one_or_zero(a, b):
    @lru_cache(None)
    def min_dist(s1, s2, is_one):
        if s1 == len(a) or s2 == len(b):
            return len(a) - s1 + len(b) - s2 + int(is_one) <= 1
        # no change required
        if a[s1] == b[s2]:
            return min_dist(s1 + 1, s2 + 1, is_one)
        if is_one:
            return False
        return min_dist(s1, s2 + 1, True) or min_dist(s1 + 1, s2, True) or min_dist(s1 + 1, s2 + 1, True)
    return min_dist(0, 0, False)


@lru_cache(None)
def mozni_predhodniki(s):
    output = set()
    output.add(s)
    # dodajanje (vrivanje) ene stevke
    for i in range(len(s) + 1):
        for nadomestna_stevka in range(10):
            if i == 0 and nadomestna_stevka == 0:
                continue
            if i == len(s):
                naslednji_niz = s + str(nadomestna_stevka)
            else:
                naslednji_niz = s[:i] + str(nadomestna_stevka) + s[i:]
            output.add(naslednji_niz)

    # odstranjevanje ene stevke
    for i in range(len(s)):
        naslednji_niz = s[:i]
        if i != len(s)-1:
            naslednji_niz += s[i+1:]
        output.add(naslednji_niz)

    # zamenjava ene stevke z eno drugo
    for i in range(len(s)):
        for nadomestna_stevka in range(10):
            if i == 0 and nadomestna_stevka == 0:
                continue
            naslednji_niz = s[:i] + str(nadomestna_stevka)
            if i != len(s)-1:
                naslednji_niz += s[i+1:]
            output.add(naslednji_niz)
    return output


def preberi_podatke():
    stevila = []
    while True:
        try:
            stevila.append(input().strip())
        except EOFError:
            break
    return stevila


stevila = preberi_podatke()
n = len(stevila)


# Podproblem: f(i) ... najdaljša pot do i-tega števila
@lru_cache(None)
def f(i):
    if i == 0:
        return 1
    if i >= n:
        return f(n-1)
    # PRVI NAČIN: Poiscemo stevila, ki imajo Levenstheinovo razdaljo 0 ali 1
    # mozni_nasledniki = [j for j in range(0, i) if lev_dist_one_or_zero(stevila[i], stevila[j])]
    # DRUGI NAČIN: Generiramo množico vseh možnih števil z levenstheinovo razdaljo stran za 0 ali 1,
    # ter se sprehodimo po j= 0, 1, ..., i-1 ter pogledamo če je stevilo[j] znotraj te mnozice
    # v funkciji mozni_predhodniki manjka en robni pogoj, ne vem pa, kateri točno.
    vsi_mozni_predhodniki = mozni_predhodniki(stevila[i])
    mozni_nasledniki = [j for j in range(0, i) if stevila[j] in vsi_mozni_predhodniki]
    if mozni_nasledniki:
        return 1 + max([f(j) for j in mozni_nasledniki])
    return 1


print(f(n-1))
