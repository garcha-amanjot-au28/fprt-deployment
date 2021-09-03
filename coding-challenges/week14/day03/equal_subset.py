def canPartition(nums):
	target, n = sum(nums), len(nums)
	if target & 1: return False
	target >>= 1
	dp = [True] + [False]*target
	for x in nums:
		dp = [dp[s] or (s >= x and dp[s-x]) for s in range(target+1)]
		if dp[target]: return True
	return False

if __name__ == '__main__':

    nums = [1,5,11,5]
    print(canPartition(nums))