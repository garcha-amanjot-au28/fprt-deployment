# Q-1 ) Climbing Stairs - solve without DP
def climbStairs(n):

    def helper(n):
        if n == 0:
            return 1
        if n < 0 :
            return 0

        return helper(n-1)+ helper(n-2)

    





    if n <= 1:
        return n
    return helper(n)

if __name__ == '__main__':
    print(climbStairs(4))