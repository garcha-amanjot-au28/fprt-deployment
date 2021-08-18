from functools import lru_cache

class Solution:

    def divisorGame(self,n):

        @lru_cache(None)
        def recur (n , player):
            
            if n <= 1 and player == True :
                return False

            if n<= 1 and player == False:
                return True

            for i in range (1,n):
                if n % i == 0:
                    return recur (n-1, not player)

        return recur (n,True)

if __name__ == '__main__':

    result = Solution()
    print(result.divisorGame(12))