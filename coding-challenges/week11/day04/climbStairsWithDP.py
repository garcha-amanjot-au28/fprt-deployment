# Q-2 )Solve above question with DP
def climbStairs(n ):

    def helper (x , n , dp):
        if x == n :
            return 1
        if x > n :
            return 0
        if dp[x] >= 0 :
            return dp[x] 
        
        ans = helper(x+1,n,dp) + helper(x+2,n,dp)
        dp[x]= ans
        return dp[x]




    dp = [-1 for _ in range (n)]
    return helper (0,n,dp)

if __name__ == '__main__':
    print(climbStairs(4))
    