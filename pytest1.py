# n - input

dsu = [i for i in range(n + 1)]
def find_dsu(x):
    if x == dsu[x]:
        return x
    else:
        dsu[x] = find_dsu(dsu[x])
        return dsu[x]
def union_dsu(x, y):
    x = find_dsu(x)
    y = find_dsu(y)
    if x != y:
        dsu[y] = x
