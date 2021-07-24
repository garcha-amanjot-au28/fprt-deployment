def lcp(strs):
    if not strs: return ""


    Min = min (strs)
    Max = max (strs)

    for idx , k in enumerate(Max):
        if k != Min[idx]:
            return Min[:idx]
    return Min

print(lcp(["flower","flow","flight"]))