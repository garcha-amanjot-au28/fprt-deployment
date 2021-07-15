
def sum(n: int):
    if n == 0:
        return 0

    m = n-1 
    if m == 0 :
        return 1


    ans = (m+1) + sum (m)
    return ans


print(sum(5))
