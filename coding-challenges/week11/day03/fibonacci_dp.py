class Solution:
    def __init__(self):
        pass

        


    def fib(self,n,np):
        if n <= 1:
            return n

        if np[n] is not None:
            return np[n]

        ans = self.fib(n-1,np) + self.fib(n-2,np)
        np[n] = ans
        return np[n]

if __name__ == '__main__':
    res = Solution()
    np = [None] * 10000
    print(res.fib(6,np))