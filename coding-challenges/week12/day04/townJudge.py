def findJudge( N, trust):
        count = [0] * (N + 1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        return -1

if __name__ == '__main__':

    N = 3
    trust = [[1,3],[2,3]]
    print(findJudge(N , trust))