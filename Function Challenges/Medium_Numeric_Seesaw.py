def numeric_seesaw(n):
    ls = []
    for i in range(1,n+1):
        ls.append(i)
    for i in range(2,n+1):
        ls.append(ls[n-i])

    return ls


def numeric_seesaw(n):
    asc = list(range(1, n + 1))
    dsc = list(range(n-1,0,-1))

    return asc+dsc
