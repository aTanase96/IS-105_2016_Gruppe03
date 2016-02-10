def find_max (L):
    if len(L) == 1:
        return L[0]
    v1 = L[0]
    v2 = find_max(L[1:])
    if v1 > v2:
        return v1
    else:
        return v2
raw_input()