def solution(arr,n) :
    h = {}
    for i in arr :
        if i in h :
            h[i] += 1
        else :
            h[i] = 1
    min_freq = min(h.values())
    max_element = max([ x for x,y in h.items() if y == min_freq ])
    return max_element
if __name__ == '__main__':
    arr = [2,2,5,50,1]
    n = 5
    print(solution(arr,n))